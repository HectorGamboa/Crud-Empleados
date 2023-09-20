from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentForm
from aplications.empleados.models import Empleado, Departamento
from django.views.generic import ListView

class NewDepartamentoView(FormView):
    # model = Departamento
    template_name = "departamento/new_departamento.html"
    form_class = NewDepartamentForm
    success_url = "/"

    def form_valid(self, form):
        print("*****-----Estamos en el form valid----******")

        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['shortname']
        )

        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']

        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job=1,
            departamento=depa
        )

        return super(NewDepartamentoView, self).form_valid(form)

class DeparamentoList(ListView):
    model = Departamento
    context_object_name = 'departamento'
    template_name='departamento/list_departamento_all.html'