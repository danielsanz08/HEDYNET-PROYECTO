from django import forms
<<<<<<< HEAD
from .models import Transaccion, Insumo, Usuario
=======
from .models import Transaccion, Insumo,Usuario

>>>>>>> ceb4bc462374777be02770693ad54b35882e81f4
class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = '__all__'
        
class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'descripcion', 'cantidad']
<<<<<<< HEAD

class UsuarioForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirma Contraseña')

    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'rol', 'telefono', 'profile_picture']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        if commit:
            usuario.set_password(self.cleaned_data.get('password1'))
            usuario.save()
        return usuario

class LoginForm(forms.Form):
    nombre = forms.CharField(label='Nombre de Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

=======
        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
>>>>>>> ceb4bc462374777be02770693ad54b35882e81f4
