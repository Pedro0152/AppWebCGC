# Generated by Django 4.1 on 2022-10-13 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Contratacion', '0008_trabajadoretapa_rename_imagen_contrato_contrato_and_more'),
        ('Facturacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='imagen',
            new_name='factura',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='codigoREEUP',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='cuenta_bancaria',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='nit',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='telefono',
        ),
        migrations.AddField(
            model_name='factura',
            name='codigo',
            field=models.PositiveIntegerField(default=0, verbose_name='código'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='factura',
            name='numero_de_contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contratacion.contrato'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='numero_de_etapa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Contratacion.etapa'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='numero_de_factura',
            field=models.CharField(max_length=20, verbose_name='número de factura'),
        ),
    ]