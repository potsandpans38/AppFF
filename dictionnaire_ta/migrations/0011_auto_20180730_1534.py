# Generated by Django 2.0.7 on 2018-07-30 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionnaire_ta', '0010_auto_20180728_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='variable',
            name='lgr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='numero',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
    ]
