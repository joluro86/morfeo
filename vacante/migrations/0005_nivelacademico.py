# Generated by Django 5.1.4 on 2025-03-14 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacante', '0004_campoespecificopregrado'),
    ]

    operations = [
        migrations.CreateModel(
            name='NivelAcademico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=300, unique=True)),
            ],
            options={
                'verbose_name': 'Nivel Académico',
                'verbose_name_plural': 'Niveles Académicos',
            },
        ),
    ]
