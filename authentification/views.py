from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from datetime import date, timedelta

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework import generics, permissions, status, views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentification.renderers import UserRenderers
from authentification.token import get_token_for_user
from authentification.serializers import *


class UserLoginView(APIView):
    render_classes = [UserRenderers]

    def post(self, request, format=None):
        serializers = UserLoginSerializers(data=request.data, partial=True)
        if serializers.is_valid(raise_exception=True):
            username = serializers.data['username']
            password = serializers.data['password']
            if username == '' and password == '':
                return Response({'error': {'none_filed_error': ['Username or password is not write']}},
                                status=status.HTTP_204_NO_CONTENT)
            user = authenticate(username=username, password=password)
            if user is None:
                return Response({'error': {'none_filed_error': ['Username or password is not valid']}},
                                status=status.HTTP_404_NOT_FOUND)
            else:
                token = get_token_for_user(user)
                return Response({'token': token}, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfilesView(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def get(self, request, format=None):
        serializers = UserPorfilesSerializers(request.user)
        return Response({'msg': serializers.data}, status=status.HTTP_200_OK)


class UserDetailsView(APIView):
    render_classes = [UserRenderers]
    perrmisson_class = [IsAuthenticated]

    def put(self, request, format=None):
        serializers = UserDetailsSerializers(instance=request.user, data=request.data, partial=True, )
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'msg': serializers.data}, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if self.request.data.get('all'):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"status": "OK, goodbye, all refresh tokens blacklisted"})
        refresh_token = self.request.data.get('refresh_token')
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"status": "OK, goodbye"})