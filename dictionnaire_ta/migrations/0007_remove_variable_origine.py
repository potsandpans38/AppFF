# Generated by Django 2.0.7 on 2018-07-28 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionnaire_ta', '0006_variable_origine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variable',
            name='origine',
        ),
    ]