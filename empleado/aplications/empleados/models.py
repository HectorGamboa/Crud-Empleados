from django.db import models
from aplications.departamentos.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades ( models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    class Meta:
        verbose_name="Habilidad"
        verbose_name_plural = 'Habilidades empleado'
        ordering=['habilidad']
    def __str__(self):
        return str(self.id)+'-'+ self.habilidad


class Empleado (models.Model):
    Job_Choices = (
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','otro'),
        )
    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    full_name = models.CharField('Nombre Completo', max_length=100, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=Job_Choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado',blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida= RichTextField()
    class Meta:
        verbose_name='Mi Empelado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering=['first_name']
        unique_together= ['first_name','last_name']
    def __str__(self):
        return str(self.id)+'-'+ self.first_name+'-'+self.last_name