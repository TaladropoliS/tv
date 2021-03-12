from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
    path('crear_programa', views.crear),
    path('programa/', views.programa),
    path('ver/<int:id>', views.ver),
    path('editar/<int:id>', views.editar),
    path('borrar/<int:id>', views.borrar),
    path('programas/', views.programas),
    ]