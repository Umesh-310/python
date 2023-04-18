from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, RegisterSerializer, UserProfileSerializer, TokenPairSerializer, UserSignUpSerializer
from .models import User, UserProfile
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Create your views here.

# ///// Create user and return Token /////


class UserDetail(generics.CreateAPIView):
    serializer_class = UserSignUpSerializer

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
            UserProfile.objects.create(user=user)
            # generate tokens
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            # add the tokens to the response
            token_serializer = TokenPairSerializer(
                {'refresh': str(refresh), 'access': str(access)})
            tokens = token_serializer.data
            serializer.validated_data['tokens'] = tokens

            return Response(serializer.validated_data['tokens'],)
        return Response(status=400, data=serializer.errors)


#  user profile and Update

3


class UserDetailUpdate(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get(self, request):
        user = request.user
        queryset = UserProfile.objects.filter(user=user)
        serializer_class = UserProfileSerializer(queryset, many=True)
        return Response(serializer_class.data[0])

    def put(self, request, *args, **kwargs):
        user = request.user
        userProfile = UserProfile.objects.get(user=user)
        userprofile_serializer = UserProfileSerializer(
            userProfile, data=request.data, many=False)
        if userprofile_serializer.is_valid():
            userprofile_serializer.save()
            return Response(userprofile_serializer.data)
        else:
            return Response(userprofile_serializer.errors)

# allow user to login with email and username and create token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(['GET'])
def UserGiveAToken(request, email):
    user = User.objects.filter(email=email).first()
    if user:
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        # add the tokens to the response
        token_serializer = TokenPairSerializer(
            {'refresh': str(refresh), 'access': str(access)})
        tokens = token_serializer.data

        # serializer = RegisterSerializer(queryset)
        return Response(status=200, data=tokens)

    return Response(status=400, data=False)
