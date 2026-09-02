from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('reparaciones/', views.lista_reparaciones, name='lista_reparaciones'),
    path('reparaciones/nueva/', views.nueva_reparacion, name='nueva_reparacion'),
    path('reparaciones/editar/<int:id>/', views.editar_reparacion, name='editar_reparacion'),
    path('reparaciones/eliminar/<int:id>/', views.eliminar_reparacion, name='eliminar_reparacion'),
]