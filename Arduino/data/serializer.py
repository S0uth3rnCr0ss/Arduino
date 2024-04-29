from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Data


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ["id", "username", "password", "email"]


# class DataSerializer(serializers.ModelSerializer):
#     class Meta(object):
#         model = Data
#         field = ["AirQualityIndex"]


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"
