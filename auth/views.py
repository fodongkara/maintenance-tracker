from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from auth.serializers import UserSerializer 
from rest_framework.permissions import AllowAny,IsAdminUser

class UserViewSet(ModelViewSet):
    """API Endpoint for viewing and editting user details"""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ['put', 'patch', 'get', 'delete']

class UserRegisterViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ['post']
