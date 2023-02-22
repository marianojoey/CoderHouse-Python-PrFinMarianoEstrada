from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FNotas(forms.Form):
    f_titulo = forms.CharField()
    f_descripcion= forms.CharField()
    f_autor= forms.CharField()
    f_cuerpo= forms.Textarea()
    f_fecha_publ=forms.DateField()

class FPeriodistas(forms.Form):
    f_nombre_apel=forms.CharField()
    f_email=forms.EmailField()
    f_es_editor=forms.BooleanField()

class FRegistro(UserCreationForm):
    username=forms.CharField(label="Usuario/Alias",help_text="<br>Máximo 150 caracteres.<br>No se pueden usar caracteres especiales.")
    first_name=forms.CharField(label="Nombre/s")
    last_name=forms.CharField(label="Apellido/s")
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label= "Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]