from .models import Morador
from django.forms import ModelForm


class MoradorForm(ModelForm):
     
    class Meta:
        model = Morador
        fields = "__all__"