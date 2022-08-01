from django.contrib import admin
from .models import Morador, Aviso, Reuniao, Reclamacao, Reserva

admin.site.register([Morador, Aviso, Reuniao, Reclamacao, Reserva])

