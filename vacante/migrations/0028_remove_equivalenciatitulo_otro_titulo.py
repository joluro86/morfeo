# Generated by Django 5.1.4 on 2025-03-28 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacante', '0027_equivalenciatitulo_otro_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equivalenciatitulo',
            name='otro_titulo',
        ),
    ]
