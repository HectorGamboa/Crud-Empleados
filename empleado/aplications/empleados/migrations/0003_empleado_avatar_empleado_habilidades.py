# Generated by Django 4.2 on 2023-04-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_habilidades_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='empleados.habilidades'),
        ),
    ]
