# Generated by Django 4.1 on 2022-10-13 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Entrada_de_datos', '0005_cliente_empresa_matriz_alter_cliente_codigoreeup_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajador',
            name='apellidos',
        ),
    ]