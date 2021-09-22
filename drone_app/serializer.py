from rest_framework import serializers
from .models import *
from django.db.models.query_utils import Q
from rest_framework import serializers
from . models import *
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator


class CustomUserSerializer(serializers.ModelSerializer):           #CostumUser SERIALIZER .
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'user_role')
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Not a user Details.")


class CustomUserRegisterSerializer(serializers.ModelSerializer):   #CostumUser REGISTER SERIALIZER .
    username = serializers.CharField()
    email = serializers.EmailField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(min_length=6, write_only=True)
    user_role = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'user_role')  #.... user_role  check
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = validated_data.get('email')
        username = validated_data.get('username')
        password = validated_data.pop('password', None)
        user_role = validated_data.get('user_role')
        instance = CustomUser.objects.create(email=email, username=username, user_role=user_role)
        if password is not None:
            instance.set_password(password)
        instance.is_superuser = True
        instance.is_staff = True
        instance.save()
        return instance

class CustomUserupdelSerializer(serializers.ModelSerializer):        #CostumUser Edit SERIALIZER .
    username = serializers.CharField()
    email = serializers.EmailField(required=True)
    user_role = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_role')  #.... user_role  check


class CustomUserLoginSerializer(serializers.Serializer):      #CostumUser Login Validation SERIALIZER .
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")

class CustomUserChangePasswordSerializer(serializers.Serializer):    #CostumUser Password SERIALIZER .
    model = CustomUser

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)


class DronesCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DronesCategory
        fields = ("id", "url", "name")

class DronesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drones
        fields = ("id", "url", "name", "drone_category", "manufacture_date", "is_participated", "created_at")

class PilotsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pilots
        fields = ("id", "url", "name", "gender", "number_race", "created_at")

class CompetitionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competitions
        fields = ("id", "url", "drone", "pilot", "distance", "date")
