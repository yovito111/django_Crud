# Generated by Django 4.1 on 2022-08-05 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(null=True),
        ),
    ]
