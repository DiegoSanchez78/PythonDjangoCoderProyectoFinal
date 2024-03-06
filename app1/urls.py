from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.inicio , name='index'),
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/', views.mostrar_cursos, name='cursos'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('profesores/', views.profesores,name='profesores'),
    path('form-curso/', views.form_curso, name='formCurso'),
    path('form-curso-2/', views.form_curso_2, name='formCurso2'),
    path('buscar/', views.buscar, name='buscar'),
    path('contactos/', views.contactos, name='contactos'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobreNosotros'),
]

urlpatterns += [
    path('clases/curso/', views.CursosListView.as_view(), name='inicio'),
    path('clases/curso/create/', views.CursosCreateView.as_view(), name='create'),
    path('clases/curso/update/<int:pk>/', views.CursosUpdateView.as_view(), name='update'),
    path('clases/curso/delete/<int:pk>/', views.CursosDeleteView.as_view(), name='delete'),
    path('clases/curso/detail/<int:pk>/', views.CursosDetailView.as_view(), name='detail'),
]