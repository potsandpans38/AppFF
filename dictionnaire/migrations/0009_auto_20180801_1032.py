# Generated by Django 2.0.7 on 2018-08-01 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionnaire', '0008_auto_20180801_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='variable',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='doc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='fiabilite',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='lgr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='millesime',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='modalites',
            field=models.ManyToManyField(to='dictionnaire.DescVariable'),
        ),
        migrations.AddField(
            model_name='variable',
            name='nat',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='nom',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='observation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='origine',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='table_associee',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='variable',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
