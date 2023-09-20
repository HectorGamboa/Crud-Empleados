from django.db import models

# Create your models here.

class prueba (models.Model):
    title = models.CharField( max_length=30)
    subtitle = models.CharField( max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.title +'-'+self.subtitle