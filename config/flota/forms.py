from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Vehiculo, Asignacion
from django.contrib.auth import authenticate
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Contraseña")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Nombre de usuario o contraseña incorrectos.")
        return cleaned_data


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = '__all__'
        
