from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_reparaciones, name='lista_reparaciones'),
    path('nueva/', views.nueva_reparacion, name='nueva_reparacion'),
]