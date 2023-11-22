from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.exceptions import AuthenticationFailed


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'id']


class UserLoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserPorfilesSerializers(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['username', 'groups', 'first_name', 'last_name', ]


class UserDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'groups', 'first_name', 'last_name']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance 