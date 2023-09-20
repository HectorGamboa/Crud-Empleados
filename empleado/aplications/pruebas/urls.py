from django.urls import path
from . import views

urlpatterns = [
      path('pruebas/',  views.IndexView.as_view()),
      path('pruebas/resumen_fundation',  views.ResumenFundationView.as_view(),name='resumen_fundation'),
      path('pruebas/list',  views.ListView.as_view()),
      path('pruebas/lista_prueba', views.ModeloPruebaListView.as_view()),
      path('pruebas/add', views.PruebaCreateView.as_view(), name='prueba_add'),
]
