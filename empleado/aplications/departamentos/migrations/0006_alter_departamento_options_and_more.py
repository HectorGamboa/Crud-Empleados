# Generated by Django 4.2 on 2023-04-26 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0005_alter_departamento_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Mi Departamento', 'verbose_name_plural': 'Areas de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'short_name')},
        ),
    ]
