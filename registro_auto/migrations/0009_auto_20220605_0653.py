# Generated by Django 3.2.11 on 2022-06-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_auto', '0008_alter_unirmeregistro_millas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unirmeregistro',
            name='locacion',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='unirmeregistro',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
    ]
