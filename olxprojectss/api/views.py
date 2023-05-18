from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from api.serializers import Userserializer
from django.contrib.auth.models import User
# Create your views here.
class Usercreation(GenericViewSet,CreateModelMixin):
    serializer_class=Userserializer
    queryset=User.objects.all()