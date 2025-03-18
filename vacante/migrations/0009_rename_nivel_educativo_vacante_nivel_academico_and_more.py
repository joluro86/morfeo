# Generated by Django 5.1.4 on 2025-03-18 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacante', '0008_vacante'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacante',
            old_name='nivel_educativo',
            new_name='nivel_academico',
        ),
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
        migrations.RemoveField(
            model_name='vacante',
            name='posgrado',
        ),
        migrations.CreateModel(
            name='VacanteCampo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo_amplio_posgrado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacante.campoamplioposgrado')),
                ('campo_amplio_pregrado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacante.campoampliopregrado')),
                ('campo_detallado_posgrado', models.ManyToManyField(blank=True, to='vacante.campodetalladoposgrado')),
                ('campo_detallado_pregrado', models.ManyToManyField(blank=True, to='vacante.campodetalladopregrado')),
                ('campo_especifico_posgrado', models.ManyToManyField(blank=True, to='vacante.campoespecificoposgrado')),
                ('campo_especifico_pregrado', models.ManyToManyField(blank=True, to='vacante.campoespecificopregrado')),
                ('posgrado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posgrados_vacantes', to='vacante.nivelacademico')),
                ('vacante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campos_vinculados', to='vacante.vacante')),
            ],
        ),
    ]
