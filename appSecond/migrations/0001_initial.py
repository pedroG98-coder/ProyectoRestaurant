# Generated by Django 4.0.6 on 2022-07-15 18:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre(s)')),
                ('apellido_paterno', models.CharField(max_length=100, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=100, verbose_name='Apellido Materno')),
                ('calle', models.CharField(default='', max_length=50, verbose_name='Calle')),
                ('ciudad', models.CharField(default='', max_length=50, verbose_name='Ciudad')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('cp', models.CharField(default='', max_length=10, verbose_name='Código Postal')),
                ('telefono', models.CharField(default='', max_length=12, unique=True, verbose_name='Telefono')),
                ('fecha_elaboracion', models.DateTimeField(auto_now_add=True)),
                ('estatus_sistema', models.BooleanField(default=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_pedidos', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)], verbose_name='Cantidad de Pedidos')),
                ('fecha_elaboracion', models.DateTimeField(auto_now_add=True)),
                ('estatus_sistema', models.BooleanField(default=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('id_cliente', models.ManyToManyField(to='appSecond.cliente')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_platillo', models.CharField(max_length=100, unique=True, verbose_name='Nombre del Platillo')),
                ('precio_platillo', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Precio del Platillo')),
                ('bebida', models.CharField(max_length=100, verbose_name='Nombre de la Bebida')),
                ('precio_bebida', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Precio de la Bebida')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción del Platillo')),
                ('fecha_elaboracion', models.DateTimeField(auto_now_add=True)),
                ('estatus_sistema', models.BooleanField(default=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('id_pedido', models.ManyToManyField(to='appSecond.pedido')),
            ],
            options={
                'verbose_name': 'Platillo',
                'verbose_name_plural': 'Platillos',
            },
        ),
        migrations.CreateModel(
            name='Mesero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre(s)')),
                ('apellido_paterno', models.CharField(max_length=100, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=100, verbose_name='Apellido Materno')),
                ('domicilio', models.CharField(default='', max_length=50, verbose_name='Domicilio')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('telefono', models.CharField(default='', max_length=12, verbose_name='Telefono')),
                ('fecha_elaboracion', models.DateTimeField(auto_now_add=True)),
                ('estatus_sistema', models.BooleanField(default=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('id_pedido', models.ManyToManyField(to='appSecond.pedido')),
            ],
            options={
                'verbose_name': 'Mesero',
                'verbose_name_plural': 'Meseros',
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_personas', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Numero de Personas')),
                ('fecha_elaboracion', models.DateTimeField(auto_now_add=True)),
                ('estatus_sistema', models.BooleanField(default=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appSecond.cliente')),
            ],
            options={
                'verbose_name': 'Mesa',
                'verbose_name_plural': 'Mesas',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importe', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000)], verbose_name='Importe Total')),
                ('fecha_elaboracion', models.DateTimeField(auto_now_add=True)),
                ('estatus_sistema', models.BooleanField(default=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('id_pedido', models.ManyToManyField(to='appSecond.pedido')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
    ]
