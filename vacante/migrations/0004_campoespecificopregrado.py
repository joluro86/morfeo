# Generated by Django 5.1.4 on 2025-03-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacante', '0003_rename_campoamplio_campoampliopregrado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampoEspecificoPregrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=300, unique=True)),
            ],
            options={
                'verbose_name': 'Campo Especifico',
                'verbose_name_plural': 'Campos Especificos',
            },
        ),
    ]
