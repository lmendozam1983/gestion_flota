from django.urls import path
from . import views
urlpatterns = [
    path('usuarios/nuevo/', views.usuario_nuevo, name='usuario_nuevo'),
    path('usuarios/', views.usuarios_lista, name='usuarios'),
    path('login/', views.signin_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('vehiculos/', views.vehiculo_lista, name='vehiculos'),
    path('vehiculos/nuevo/', views.vehiculo_nuevo, name='vehiculo_nuevo'),
    path('vehiculos/editar/<int:id>/', views.vehiculo_editar, name='vehiculo_editar'),
    path('vehiculos/eliminar/<int:id>/', views.vehiculo_eliminar, name='vehiculo_eliminar'),
    path('asignaciones/', views.asignacion_lista, name='asignaciones'),
    path('asignaciones/nueva/', views.asignacion_nueva, name='asignacion_nueva'),
    path('asignaciones/editar/<int:id>/', views.asignaciones_editar, name='asignaciones_editar'),
    path('asignaciones/eliminar/<int:id>/', views.asignaciones_eliminar, name='asignaciones_eliminar'),
]