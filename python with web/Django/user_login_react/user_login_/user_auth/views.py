from django.template import loader
from .models import UserProfile, Image, UserAdd
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import User, UserProfileSerializer, TokenPairSerializer, UserSignUpSerializer, MultiModelSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

# // mail import
from django.core.mail import send_mail
from django.conf import settings

# // otp import
from django_otp.oath import totp
from django_otp.oath import TOTP
from django_otp.util import random_hex
from unittest import mock
import time


secret_key = b'1234567890123467890'
now = int(time.time())


# ///////////////////////////////////////////////////////////////////////////////////

class TOTPVerification:

    def __init__(self):
        # secret key that will be used to generate a token,
        # User can provide a custom value to the key.
        # self.key = random_hex(20).encode()
        self.key = b'1234567890123467890'
        # counter with which last token was verified.
        # Next token must be generated at a higher counter value.
        self.last_verified_counter = -1
        # this value will return True, if a token has been successfully
        # verified.
        self.verified = False
        # number of digits in a token. Default is 6
        self.number_of_digits = 6
        # validity period of a token. Default is 30 second.
        self.token_validity_period = 60

    def totp_obj(self):
        # create a TOTP object
        totp = TOTP(key=self.key,
                    step=self.token_validity_period,
                    digits=self.number_of_digits)
        # the current time will be used to generate a counter
        totp.time = time.time()
        return totp

    def generate_token(self):
        # get the TOTP object and use that to create token
        totp = self.totp_obj()
        # token can be obtained with `totp.token()`
        token = str(totp.token()).zfill(6)
        return token

    def verify_token(self, token, tolerance=0):
        try:
            # convert the input token to integer
            token = int(token)
        except ValueError:
            # return False, if token could not be converted to an integer
            self.verified = False
        else:
            totp = self.totp_obj()
            # check if the current counter value is higher than the value of
            # last verified counter and check if entered token is correct by
            # calling totp.verify_token()
            if ((totp.t() > self.last_verified_counter) and
                    (totp.verify(token, tolerance=tolerance))):
                # if the condition is true, set the last verified counter value
                # to current counter value, and return True
                self.last_verified_counter = totp.t()
                self.verified = True
            else:
                # if the token entered was invalid or if the counter value
                # was less than last verified counter, then return False
                self.verified = False
        return self.verified


# from django.http
# Create your views here.
mail_otp = TOTPVerification()


@api_view(['POST'])
def sendMail(request):
    subject = 'welcome to NEW world'
    message = "Thanks"
    html_message = loader.render_to_string(
        './otpTemp.html',
        {
            'name': "umesh",
            'otp':  mail_otp.generate_token(),
        }
    )
    # message = otptemp("umesh", mail_otp.generate_token())
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.data['email'], ]
    send_mail(subject, message, email_from,
              recipient_list, html_message=html_message,)
    return Response({"id": "hello"})


@api_view(['POST'])
def checkOtp(request):
    otp = request.data['otp']
    check = mail_otp.verify_token(token=otp)
    print(check)
    print(mail_otp.token_validity_period)
    return Response({"id": "hello"})


# ////////////////////////////////////////////////////////////////


class UserProfileList(generics.ListCreateAPIView):
    # queryset = UserProfile.objects.all()
    # serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request):

        user = request.user
        queryset = UserProfile.objects.filter(user=user)
        serializer_class = UserProfileSerializer(queryset, many=True)
        return Response(serializer_class.data)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # queryset = Image.objects.all()
    # serializer_class = ImageSerializer
    # queryset = UserAdd.objects.all()
    # serializer_class = UseraddressSerializer


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def addStudentname(request):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer(queryset, many=True)
    return Response(serializer_class.data)


class MultiCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MultiModelSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        blog_serializer = MultiModelSerializer(data=data, many=False)
        if blog_serializer.is_valid():
            userProfile_data = blog_serializer.validated_data['userProfile']
            userProfile_data['user'] = request.user
            image_data = blog_serializer.validated_data['image']
            image_data['user_i'] = request.user
            address_data = blog_serializer.validated_data['address']
            address_data['user_a'] = request.user

            UserProfile.objects.create(**userProfile_data)
            Image.objects.create(**image_data)
            UserAdd.objects.create(**address_data)
            return Response({"data": blog_serializer.data})
        else:
            return Response(blog_serializer.errors)


class UserSignUpView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            # create the user
            user_data = serializer.validated_data['user']
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
            )

            # generate tokens
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            # add the tokens to the response
            token_serializer = TokenPairSerializer(
                {'refresh': str(refresh), 'access': str(access)})
            tokens = token_serializer.data
            serializer.validated_data['tokens'] = tokens

            return Response(serializer.validated_data,)
        return Response(serializer.errors,)
