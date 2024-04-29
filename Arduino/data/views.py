from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Data
from .serializer import DataSerializer, UserSerializer

from django.shortcuts import get_object_or_404

# from .serializers import UserSerializer, DeviceSerializer, DeviceFullSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# from serializer import DataSerializer,UserSerializer
# Create your views here.


@api_view(["POST"])
def postUNOdata(request):
    data = request.data.copy()
    serializer = DataSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"status": 200, "data": serializer.data}, status=status.HTTP_201_CREATED
        )


@api_view(["GET"])
def home(request):
    user_obj = User.objects.all()
    serializer = UserSerializer(user_obj, many=True)
    return Response({"status": 200, "data": serializer.data})


@api_view(["POST"])
def login(request):
    try:
        user = User.objects.get(username=request.data["username"])
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    if not user.check_password(request.data["password"]):
        return Response(
            {"detail": "Incorrect password."}, status=status.HTTP_400_BAD_REQUEST
        )

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})


@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data["username"])
        user.set_password(request.data["password"])
        token = Token.objects.create(user=user)
        user.save()
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
