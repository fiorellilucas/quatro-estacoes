from rest_framework import viewsets, permissions

from . import models, serializers

# api views


class MoradorViewSet(viewsets.ModelViewSet):

    queryset = models.Morador.objects.all()
    serializer_class = serializers.MoradorSerializer
    permission_classes = [permissions.AllowAny]


class ReservaViewSet(viewsets.ModelViewSet):

    queryset = models.Reserva.objects.all()
    serializer_class = serializers.ReservaSerializer
    permission_classes = [permissions.AllowAny]


class ReuniaoViewSet(viewsets.ModelViewSet):

    queryset = models.Reuniao.objects.all()
    serializer_class = serializers.ReuniaoSerializer
    permission_classes = [permissions.AllowAny]


class AvisoViewSet(viewsets.ModelViewSet):

    queryset = models.Aviso.objects.all()
    serializer_class = serializers.AvisoSerializer
    permission_classes = [permissions.AllowAny]


class ReclamacaoViewSet(viewsets.ModelViewSet):

    queryset = models.Reclamacao.objects.all()
    serializer_class = serializers.ReclamacaoSerializer
    permission_classes = [permissions.AllowAny]
