from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.login_request, name='Login'),
    path('edit/', views.edit, name='Edit'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='app1/index.html'), name="Logout"),
    path('editar_usuario/', views.edit, name='EditarUsuario'),
    path('agregar_avatar/', views.agregar_avatar, name='Agregar_avatar'),
]