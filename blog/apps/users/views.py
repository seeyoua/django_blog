from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin
from .serializers import CreateUserSerializer

# Create your views here.




#用户注册
class ReuserView(CreateAPIView):

    serializer_class = CreateUserSerializer
