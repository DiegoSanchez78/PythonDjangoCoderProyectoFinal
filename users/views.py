from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import  UserRegisterForm
from django.contrib.auth.decorators import login_required
from users.forms import UserEditForm,UserRegisterForm
from users.forms import AvatarFormulario
from django.contrib.auth.models import User
from users.models import Avatar

# Create your views here.

def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "app1/index.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})


def register(request):
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"app1/index.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})

@login_required
def edit(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            if informacion["password1"] != informacion["password2"]:
                datos = {
                    'first_name': usuario.first_name,
                    'email': usuario.email
                }
                miFormulario = UserEditForm(initial=datos)

            else:
                usuario.email = informacion['email']
                if informacion["password1"]:
                    usuario.set_password(informacion["password1"])
                usuario.last_name = informacion['last_name']
                usuario.first_name = informacion['first_name']
                usuario.save()

                # Creamos nueva imagen en la tabla
                # try:
                #     avatar = Imagen.objects.get(user=usuario)
                # except Imagen.DoesNotExist:
                #     avatar = Imagen(user=usuario, imagen=informacion["imagen"])
                #     avatar.save()
                # else:
                #     avatar.imagen = informacion["imagen"]
                #     avatar.save()

                return render(request, "App1/index.html")

    else:
        datos = {
            'last_name': usuario.last_name,
            'first_name': usuario.first_name,
            'email': usuario.email
        }
        miFormulario = UserEditForm(initial=datos)

    return render(request, "users/edit.html", {"mi_form": miFormulario, "usuario": usuario})

@login_required
def agregar_avatar(request):

    if request.method == 'POST':
        mi_form = AvatarFormulario(request.POST, request.FILES)

        if mi_form.is_valid():
            user = User.objects.get(username=request.user)
            try:
                avatar = Avatar.objects.get(user=user)
            except Avatar.DoesNotExist:
                avatar = Avatar(user=user, imagen=mi_form.cleaned_data['imagen'])
            else:
                avatar.imagen = mi_form.cleaned_data['imagen']
            
            avatar.save()

            return render(request, "app1/index.html")
    else:
        mi_form = AvatarFormulario()

    context_data = {'mi_form': mi_form}
    return render(request, "users/agregar_avatar.html", context_data)

