# Generated by Django 2.0.7 on 2018-07-19 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionnaire', '0004_auto_20180718_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='descvariable',
            old_name='depuis_millesime',
            new_name='millesime',
        ),
        migrations.RemoveField(
            model_name='descvariable',
            name='jusque_millesime',
        ),
    ]
