# Generated by Django 5.1.4 on 2025-03-14 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacante', '0002_alter_campoamplio_descripcion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CampoAmplio',
            new_name='CampoAmplioPregrado',
        ),
        migrations.AlterModelOptions(
            name='campoampliopregrado',
            options={'verbose_name': 'Campo Amplio Pregado', 'verbose_name_plural': 'Campos Amplios Pregrado'},
        ),
    ]
