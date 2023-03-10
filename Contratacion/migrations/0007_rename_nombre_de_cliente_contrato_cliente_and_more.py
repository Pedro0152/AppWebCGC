# Generated by Django 4.1 on 2022-10-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contratacion', '0006_remove_contrato_codigoreeup_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contrato',
            old_name='nombre_de_cliente',
            new_name='cliente',
        ),
        migrations.RemoveField(
            model_name='etapa',
            name='id',
        ),
        migrations.AddField(
            model_name='contrato',
            name='cargo',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contrato',
            name='representante',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etapa',
            name='numero_de_etapa',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='etapa',
            name='duracion',
            field=models.PositiveSmallIntegerField(verbose_name='duracion(meses)'),
        ),
    ]
