# Generated by Django 4.1 on 2022-09-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrada_de_datos', '0002_alter_categoria_docente_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='nombre',
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre_cliente',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='nombre de cliente'),
        ),
    ]
