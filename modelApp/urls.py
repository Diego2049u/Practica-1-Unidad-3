from django.urls import path
from . import views

app_name = "trabajadores"

urlpatterns = [
    path('', views.index, name='agregar'),
    path('empleados/', views.listar_empleados, name='empleados'),
    path('actualizarEmpleado/<int:id>',views.editar_empleado, name='editar'),
    path('eliminarEmpleado/<int:id>',views.eliminar_empleado, name='eliminar'),
]