# Generated by Django 3.2.11 on 2022-06-02 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicios',
            name='icono',
            field=models.CharField(default='n/a', max_length=20),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='actualizado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='contenido',
            field=models.CharField(max_length=500),
        ),
    ]
