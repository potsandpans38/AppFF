# Generated by Django 2.0.7 on 2018-07-30 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionnaire_ta', '0011_auto_20180730_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='variable',
            name='observation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
