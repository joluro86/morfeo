# Generated by Django 5.1.4 on 2025-03-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacante', '0006_campodetalladopregrado'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampoAmplioPosgrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, default='', max_length=300, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Campo Amplio Posgrado',
                'verbose_name_plural': 'Campos Amplios Posgrado',
            },
        ),
        migrations.CreateModel(
            name='CampoDetalladoPosgrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=300, unique=True)),
            ],
            options={
                'verbose_name': 'Campo Detallado Posgrado',
                'verbose_name_plural': 'Campos Detallados Posgrado',
            },
        ),
        migrations.CreateModel(
            name='CampoEspecificoPosgrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=300, unique=True)),
            ],
            options={
                'verbose_name': 'Campo Específico Posgrado',
                'verbose_name_plural': 'Campos Específicos Posgrado',
            },
        ),
    ]
