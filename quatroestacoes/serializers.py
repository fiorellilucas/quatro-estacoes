from rest_framework import serializers
from .models import Aviso, Morador, Reclamacao, Reserva, Reuniao


class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = "__all__"


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"
        depth = 1


class ReuniaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reuniao
        fields = "__all__"


class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviso
        fields = "__all__"


class ReclamacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamacao
        fields = "__all__"
