from django.urls import path
from . import views




app_name='empleado_app'

urlpatterns = [
     path('',  views.inicioView.as_view(),name="home"),
      path('listar-todo-empleados/',  views.ListAllEmpleados.as_view(),name='empleados_all'),
      path('listar-todo-empleados-admin/',  views.ListAllEmpleadosAdmin.as_view(),name='empleados_all_admin'),
      path('listar-por-areas/<shortname>',  views.ListEmpleadosAreas.as_view(),name="empleados_area"),
      path('listar-por-trabajos/<job>',  views.ListEmpleadosTrabajo.as_view()),
      path('buscar-empleado/',  views.ListEmpleadoByKword.as_view()),
      path('listar-habilidades-empleado/',  views.ListHabilidadesEmpleado.as_view()),
      path('ver-empleado/<pk>',  views.EmpleadoDetailView.as_view(),name="empleado_detail"),
      path('create-empleado/',  views.EmpleadoCreateView.as_view(),name='create_empleado'),
      path('success/',  views.Success.as_view(),name="correcto"),
      path('update/<pk>',  views.EmpleadoUpdateView.as_view(),name="edit"),
      path('delete/<pk>',  views.EmpleadoDeleteView.as_view(),name="delete"),
 ]
