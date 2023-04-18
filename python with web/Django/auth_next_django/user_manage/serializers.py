from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import User, UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class TokenPairSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()


class UserSignUpSerializer(serializers.Serializer):
    user = RegisterSerializer()
    tokens = TokenPairSerializer(read_only=True)


class UserProfileSerializer(serializers.ModelSerializer, serializers.Serializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    p_image = serializers.CharField()

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'p_image')

    def update(self, instance, validated_data):
        instance.p_image = validated_data.get(
            'p_image', instance.p_image)

        user_data = validated_data.get('user', {})
        setattr(instance.user, 'username', user_data.get(
            'username', instance.user.username))
        setattr(instance.user, 'email', user_data.get(
            'email', instance.user.email))

        instance.save()
        instance.user.save()

        return instance


class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return obj.username
        return super().default(obj)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username_or_email'

    def validate(self, attrs):
        password = attrs.get("password")
        username_or_email = attrs.get("username_or_email")

        # Authenticate the user using email or username
        user = authenticate(
            request=self.context.get("request"),
            username=username_or_email,
            password=password,
        )

        # If user is not found using username, try to find user with email
        if user is None:
            try:
                user = User.objects.get(email=username_or_email)
                user = authenticate(
                    request=self.context.get("request"),
                    username=user.username,
                    password=password,
                )
            except User.DoesNotExist:
                pass

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        if not user.is_active:
            raise serializers.ValidationError("Account is not active")

        refresh = self.get_token(user)

        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return data
