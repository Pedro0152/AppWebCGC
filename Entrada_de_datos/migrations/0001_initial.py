# Generated by Django 4.1 on 2022-09-09 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'cargo',
            },
        ),
        migrations.CreateModel(
            name='Categoria_cientifica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'categoría científica',
            },
        ),
        migrations.CreateModel(
            name='Categoria_docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'categoría docente',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.PositiveBigIntegerField()),
                ('nit', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('codigoREEUP', models.PositiveBigIntegerField(blank=True, null=True)),
                ('cuenta_bancaria', models.PositiveBigIntegerField()),
                ('titular_de_cuenta_bancaria', models.CharField(max_length=100)),
                ('sucursal', models.PositiveSmallIntegerField()),
                ('banco', models.CharField(choices=[('1', 'BANDEC'), ('2', 'BPA')], default='1', max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('municipio', models.CharField(default='Santiago de Cuba', max_length=30)),
                ('provincia', models.CharField(choices=[('1', 'Santiago de Cuba'), ('9', 'Guantánamo'), ('2', 'Las Tunas'), ('10', 'Holguín'), ('3', 'Granma'), ('11', 'Camagüey'), ('4', 'Artemisa'), ('12', 'Mayabeque'), ('5', 'Pinar del Río'), ('13', 'La Habana'), ('6', 'Isla de la Juventud'), ('14', 'Sanctis Spiritus'), ('7', 'Villa Clara'), ('15', 'Cienfuegos'), ('8', 'Matanzas'), ('16', 'Ciego de Ávila')], default='1', max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('ci', models.PositiveBigIntegerField()),
                ('telefono', models.PositiveBigIntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Categoria_cientifica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entrada_de_datos.categoria_cientifica')),
                ('Categoria_docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entrada_de_datos.categoria_docente')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entrada_de_datos.cargo')),
            ],
            options={
                'verbose_name': 'trabajador',
                'verbose_name_plural': 'trabajadores',
            },
        ),
    ]
