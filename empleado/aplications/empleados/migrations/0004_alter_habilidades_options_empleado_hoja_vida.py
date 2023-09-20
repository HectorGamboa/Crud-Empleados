# Generated by Django 4.2 on 2023-04-26 21:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_empleado_avatar_empleado_habilidades'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habilidades',
            options={'ordering': ['habilidad'], 'verbose_name': 'Habilidad', 'verbose_name_plural': 'Habilidades empleado'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
    ]