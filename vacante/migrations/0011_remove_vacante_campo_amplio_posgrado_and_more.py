# Generated by Django 5.1.4 on 2025-03-18 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacante', '0010_vacante_campo_amplio_posgrado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacante',
            name='campo_amplio_posgrado',
        ),
        migrations.RemoveField(
            model_name='vacante',
            name='campo_amplio_pregrado',
        ),
        migrations.RemoveField(
            model_name='vacante',
            name='campo_detallado_posgrado',
        ),
        migrations.RemoveField(
            model_name='vacante',
            name='campo_detallado_pregrado',
        ),
        migrations.RemoveField(
            model_name='vacante',
            name='campo_especifico_posgrado',
        ),
        migrations.RemoveField(
            model_name='vacante',
            name='campo_especifico_pregrado',
        ),
        migrations.AddField(
            model_name='vacante',
            name='numero',
            field=models.BigIntegerField(default=2, unique=True),
            preserve_default=False,
        ),
    ]
