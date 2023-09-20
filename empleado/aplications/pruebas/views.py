from django.shortcuts import render
from django.views.generic import TemplateView, ListView,CreateView
from .models import prueba
from .forms import PruebaForm
# Create your views here.


class IndexView(TemplateView):
    template_name = "pruebas/home.html"

class ResumenFundationView(TemplateView):
    template_name = "pruebas/resumen_fundation.html"


class ListView(ListView):
    template_name = 'pruebas/list.html'
    # queryset = ['A', 'B', 'C']
    context_object_name = "lista_prueba"


class ModeloPruebaListView(ListView):
    model = prueba
    template_name = 'pruebas/lista_prueba.html'
    context_object_name = 'lita_prueba'

class PruebaCreateView(CreateView):
    template_name="pruebas/add.html"
    model=prueba
    form_class = PruebaForm
    success_url = '/'