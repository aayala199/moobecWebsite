# Generated by Django 3.2.11 on 2022-06-02 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_auto', '0002_auto_20220601_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroauto',
            name='actualizado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
