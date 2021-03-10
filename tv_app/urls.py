from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
    path('crear_programa', views.crear),
    path('programa/<int:id>', views.programa)
    ]