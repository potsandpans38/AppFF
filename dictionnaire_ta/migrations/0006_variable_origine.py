# Generated by Django 2.0.7 on 2018-07-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionnaire_ta', '0005_variable_nature'),
    ]

    operations = [
        migrations.AddField(
            model_name='variable',
            name='origine',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]