from django import forms
from .models import Transaccion

class TramsaccionForm(forms.ModelForm):
    class Meta:
        model: Transaccion
        fields: 