# Generated by Django 4.1 on 2022-08-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoría', models.CharField(max_length=50, verbose_name='categoria')),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='código')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripción')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
            ],
        ),
    ]
