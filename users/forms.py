
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Avatar

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control'}), required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}), required=True)

    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}

class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput, required=False)

    last_name = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
   

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'password1', 'password2']
        help_text = {k: "" for k in fields}

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']