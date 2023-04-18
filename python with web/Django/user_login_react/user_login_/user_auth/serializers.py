from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile, Image, UserAdd
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# This is working Good


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
                  'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UseraddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAdd
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'p_image', 'user_i')


class UserProfileSerializer(serializers.ModelSerializer, serializers.Serializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    createDate = serializers.DateTimeField(
        source='user.date_joined', read_only=True)
    
    
    phone = serializers.IntegerField()
    about_self = serializers.CharField()
    DOB = serializers.DateField()
    gender = serializers.CharField()
    images = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'phone', 'about_self', 'first_name',
                  'last_name', 'DOB', 'createDate', 'gender', 'images', 'address',)

    def get_images(self, obj):
        images = Image.objects.filter(user_i=obj.user)
        return ImageSerializer(images, many=True).data

    def get_address(self, obj):
        address = UserAdd.objects.filter(user_a=obj.user)
        return UseraddressSerializer(address, many=True).data

    def update(self, instance, validated_data):
        # Update the UserProfile instance with the validated data
        instance.phone = validated_data.get('phone', instance.phone)
        instance.about_self = validated_data.get(
            'about_self', instance.about_self)
        instance.DOB = validated_data.get('DOB', instance.DOB)
        instance.gender = validated_data.get(
            'gender', instance.gender)

        instance.user.username = validated_data.get(
            'username', instance.user.username)
        instance.user.email = validated_data.get(
            'email', instance.user.email)
        instance.user.first_name = validated_data.get(
            'first_name', instance.user.first_name)
        instance.user.last_name = validated_data.get(
            'last_name', instance.user.last_name)

        # Save the updated instance
        instance.user.save()
        instance.save()

        return instance


class UserProfileOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class MultiModelSerializer(serializers.Serializer):
    userProfile = UserProfileOnlySerializer()
    image = ImageSerializer()
    address = UseraddressSerializer()


class UserCheckSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = "__all__"

# /////////////////////////////////////////////////


class TokenPairSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()


class UserSignUpSerializer(serializers.Serializer):
    user = RegisterSerializer()
    tokens = TokenPairSerializer(read_only=True)
