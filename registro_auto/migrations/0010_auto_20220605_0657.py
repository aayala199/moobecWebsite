# Generated by Django 3.2.11 on 2022-06-05 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_auto', '0009_auto_20220605_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unirmeregistro',
            name='locacion',
            field=models.CharField(choices=[('guayaquil', 'Guayaquil'), ('quito', 'Quito'), ('cuenca', 'Cuenca')], max_length=25),
        ),
        migrations.AlterField(
            model_name='unirmeregistro',
            name='year',
            field=models.IntegerField(choices=[(2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)]),
        ),
    ]
