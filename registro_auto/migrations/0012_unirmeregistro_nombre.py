# Generated by Django 3.2.11 on 2022-06-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_auto', '0011_auto_20220605_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='unirmeregistro',
            name='nombre',
            field=models.CharField(default='n/a', max_length=100),
        ),
    ]
