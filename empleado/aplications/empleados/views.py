from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView,
    TemplateView, UpdateView, DeleteView)
from django.db.models import Q
# models
from .models import Empleado
#forms
from .forms import EmpleadoForm
# funcion del home
class inicioView(TemplateView):
    """Vista que inicial conocida como home"""
    template_name = "home.html"

# Create your views here.
# Listar todos los empleados
class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    paginate_by = 5
    ordering = 'first_name'
    context_object_name='empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
        Q(first_name__icontains=palabra_clave) |
        Q(last_name__icontains=palabra_clave)
             )
        print('lista resultado', lista)
        return lista
    
#listar todos los empleados admin
# Listar todos los empleados
class ListAllEmpleadosAdmin(ListView):
    template_name = 'empleado/list_all_admin.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name='empleados'
    model=Empleado
    
#listar todos los empleados por Area
class ListEmpleadosAreas(ListView):
    template_name= 'empleado/list_por_areas.html'
    context_object_name="empleados"
    def get_queryset(self):
        #Escribimos el codigo que yo quiera
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista
    
#listar todos los empleados pór trabajo

class ListEmpleadosTrabajo(ListView):
    template_name='empleado/list_por_trabajos.html'
    context_object_name = "trabajo"
    def get_queryset(self):
        # el codigo que yo quier
        job = self.kwargs['job']
        lista = Empleado.objects.filter(
            job = job
        )
        return lista

#listar todos los empleados pór palabra clave
class ListEmpleadoByKword(ListView):
    """Lista Empleado por palabra clave"""
    template_name = "empleado/by_kword.html"
    context_object_name = "empleados"

    def get_queryset(self):
        print("*********")
        palabra_clave= self.request.GET.get('kword','')
        print("========",palabra_clave)
        lista = Empleado.objects.filter(
         first_name = palabra_clave  
        )
        print('lista resultado', lista)
        return lista
    
#listar todos los empleados por habibilidades
class ListHabilidadesEmpleado(ListView):
    template_name= "empleado/habilidades.html"
    context_object_name = "habilidades"

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model=Empleado
    template_name= "empleado/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView,self).get_context_data(**kwargs)
        context['titulo'] ='Empleado del mes'
        return context

class Success(TemplateView):
    template_name = "empleado/list_all_admin.html"

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/create_empleado.html"
    # traer todos los camposn por defecto fields=('__all__')
    form_class=EmpleadoForm
    success_url=  reverse_lazy('empleado_app:empleados_all_admin')

    def form_valid(self, form):
        #logica del codigo
        empleado = form.save( commit=False)#evita que se guarde en la base de datos solo mantengo la instancia
        empleado.full_name= empleado.first_name+" "+empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name = "empleado/update.html"
    model= Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'habilidades',
        'departamento'

        ]
    success_url=  reverse_lazy('empleado_app:empleados_all_admin') 

    def post(self, request, *args, **kwargs): 
        self.object = self.get_object()
        print("**************METODO POST*************")
        #imprimimos todo el objeto recibido de data del html
        print(request.POST)
        #interceptamos un campo en especifico
        print(request.POST['first_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print("**************Form valid*************")
        return super(EmpleadoUpdateView,self).form_valid(form)
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/delete.html"
    success_url=  reverse_lazy('empleado_app:empleados_all_admin') 