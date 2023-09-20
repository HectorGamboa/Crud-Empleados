from django.urls import path
from . import views

app_name='departamento_app'
urlpatterns = [
          path('departamento/new-departamento',views.NewDepartamentoView.as_view(), name="new_departamento"),
           path('departamento/list-departamento-all',views.DeparamentoList.as_view(), name="list_departamento_all"),

]