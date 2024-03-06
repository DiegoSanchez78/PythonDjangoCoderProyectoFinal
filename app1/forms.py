from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50 ,widget=forms.TextInput(attrs={"size": "150",'class':'form-control'}) ,label="Nombre", required=True)
    camada = forms.IntegerField(label="Camada", widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    imagen = forms.ImageField(required=False)
    detalle = forms.CharField(max_length=300 ,widget=forms.Textarea(attrs={"size": "300",'class':'form-control'}) ,label="Detalle", required=True)
    costo = forms.IntegerField(label="Costo", widget=forms.TextInput(attrs={'class':'form-control'}), required=True)

class BuscarForm(forms.Form):
    nombre = forms.CharField(max_length=25,widget=forms.TextInput(attrs={"size": "40",'class':'form-control'}),label="Ingrese el nombre del curso a buscar", required=True)

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=50 ,widget=forms.TextInput(attrs={"size": "150",'class':'form-control'}) ,label="Nombre", required=True)
    apellido = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"size": "40",'class':'form-control'}),label="Apellido", required=True)
    email = forms.EmailField( label="Email", widget=forms.EmailInput(attrs={'class':'form-control'}), required=True)
    fecha_nacimiento = forms.DateField( label="Fec nac", widget=forms.DateInput(attrs={'class':'form-control'}), required=True)
    telefono = forms.IntegerField( label="Telefono", widget=forms.TextInput(attrs={'class':'form-control'}), required=True)

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50 ,widget=forms.TextInput(attrs={"size": "150",'class':'form-control'}) ,label="Nombre", required=True)
    apellido = forms.CharField(max_length=50 ,widget=forms.TextInput(attrs={"size": "150",'class':'form-control'}) , required=True)
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control'}), required=True)
    profesion = forms.CharField(max_length=50 ,widget=forms.TextInput(attrs={"size": "150",'class':'form-control'}) ,label="Profesion", required=True)
    fecha_nacimiento = forms.DateField(label="Fec nac", widget=forms.DateInput(attrs={'class':'form-control'}), required=True)
    telefono = forms.IntegerField(label="Telefono", widget=forms.TextInput(attrs={'class':'form-control'}), required=True)

class Mostrar_cursos(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"size": "150",'class':'form-control,','placeholder':'Nombre'}), required=True)
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}), required=True)
    asunto = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"size": "150",'class':'form-control','placeholder':'Asunto'}), required=True)
    mensaje = forms.CharField(max_length=300, widget=forms.Textarea(attrs={"size": "300",'class':'form-control','placeholder':'Mensaje'}), required=True)