from django import forms
from .models import Transaccion, Insumo,u

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = '__all__'
        
class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'descripcion', 'cantidad']
        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'