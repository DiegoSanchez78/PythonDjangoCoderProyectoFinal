from django.shortcuts import render ,redirect
from app1.models import Curso ,Estudiante,Profesor
from app1.forms import CursoForm,BuscarForm,EstudianteForm,ProfesorForm,Mostrar_cursos,ContactoForm
from django.contrib.auth.decorators import login_required
# from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Avatar
from django.urls import reverse
from django.core.mail import EmailMessage


def inicio(request):
    
    
    # try:
    #     avatares = Avatar.objects.get(user=request.user.id)
    #     imagen = avatares.imagen.url
    # except:
    #     imagen = ""
    #     return render(request, 'app1/index.html', {"url": imagen})
    
    # avatares = Avatar.objects.filter(user=request.user.id)
    # return render(request, 'app1/index.html', {"url": avatares[0].imagen.url})
    
    avatares = Avatar.objects.all()

    if avatares:
       
        avatar = avatares[0]
        if avatar.imagen:
            
            print(avatar.imagen.url)
            return render(request, 'app1/index.html', {"url": avatar.imagen.url})

    
    print("No avatars or image file found.")
    return render(request, 'app1/index.html', {"url": None})


   

@login_required
def cursos(request):
    if request.method == "POST":
 
            miFormulario = CursoForm(request.POST, request.FILES)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"], detalle=informacion["detalle"], costo=informacion["costo"], imagen=informacion["imagen"])
                  curso.save()
                  return render(request, "app1/cursos.html")
    else:
            miFormulario = CursoForm()
    return render(request, "app1/cursos.html", {"formulario": miFormulario})
@login_required
def estudiantes(request):
    if request.method == "POST":
 
            miFormulario = EstudianteForm(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], fecha_nacimiento=informacion["fecha_nacimiento"], telefono=informacion["telefono"])
                  curso.save()
                  return render(request, "app1/estudiantes.html")
    else:
            miFormulario = EstudianteForm()
    return render(request, "app1/estudiantes.html", {"formulario": miFormulario})
@login_required
def profesores(request):
    if request.method == "POST":
 
            miFormulario = ProfesorForm(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"], fecha_nacimiento=informacion["fecha_nacimiento"], telefono=informacion["telefono"])
                  curso.save()
                  return render(request, "app1/profesores.html")
    else:
            miFormulario = ProfesorForm()
    return render(request, "app1/profesores.html", {"formulario": miFormulario})

@login_required
def form_curso(request):

    if request.method == 'POST':
        curso=Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
            
        curso.save()
        return render(request,"app1/index.html")
    return render(request,"app1/form-curso.html")
@login_required
def form_curso_2(request):
    if request.method == "POST":
 
            miFormulario = CursoForm(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "app1/index.html")
    else:
            miFormulario = CursoForm()
    return render(request, "app1/cursoFormulario.html", {"formulario": miFormulario})

def buscar(request):
    if request.method == 'POST':
        miFormulario = BuscarForm(request.POST) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso.objects.filter(nombre__icontains = informacion['nombre'])
            
            return render(request, "app1/buscar.html", {"cursos": curso})
    else:
         miFormulario = BuscarForm()
    return render(request, 'app1/buscar.html', {"formulario": miFormulario})

@login_required
def mostrar_cursos(request):
    if request.method == 'POST':
        miFormulario = Mostrar_cursos(request.POST) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso.objects.all()
            
            return render(request, "app1/mostrar_curso.html", {"cursos": curso})
    else:
         miFormulario = Mostrar_cursos()
    return render(request, 'app1/mostrar_curso.html', {"formulario": miFormulario})


def contactos(request): 
    contact_form = ContactoForm()
    
    if request.method == "POST":
        contact_form = ContactoForm(data=request.POST)
        if contact_form.is_valid():
            nombre = request.POST.get('nombre', '')
            email = request.POST.get('email', '')
            asunto = request.POST.get('asunto', '')
            mensaje = request.POST.get('mensaje', '')
            
            mail = EmailMessage(
             "Intituto LF : Nuevo mensaje de contacto",
             "De {} <{}><{}>\n\nEscribio:\n\n{}".format(nombre, email,asunto, mensaje),
             "LF",
             ["diegoabeydon@gmail.com"],
             reply_to=[email]
            )
            try:
                mail.send()
                return redirect(reverse('contactos')+"?ok")
            except:
                return redirect(reverse('contactos')+"?fail")

    
    
    return render(request, 'app1/contactos.html', {'form': contact_form})


from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

class CursosListView(ListView): 
    model = Curso
    template_name = 'app1/mostrar_curso.html'


class CursosCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    success_url = '/'
    fields = '__all__'

class CursosUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    success_url = '/'
    fields = ['nombre', 'camada', 'imagen', 'detalle', 'costo']

class CursosDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = '/'

class CursosDetailView(DetailView):
    model = Curso
    success_url = '/'

def sobre_nosotros(request):
        return render(request, 'app1/about.html')

