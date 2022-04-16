from django.contrib import admin
from .models import Morador, Aviso, Reuniao

admin.site.register([Morador, Aviso, Reuniao])

