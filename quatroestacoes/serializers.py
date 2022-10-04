from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Morador


class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = "__all__"
