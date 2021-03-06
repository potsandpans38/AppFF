# Generated by Django 2.0.7 on 2018-07-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DescVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('valeur', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('observation', models.CharField(blank=True, max_length=255, null=True)),
                ('depuis_millesime', models.CharField(blank=True, max_length=255, null=True)),
                ('jusque_millesime', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('lgr', models.CharField(blank=True, max_length=255, null=True)),
                ('nat', models.CharField(blank=True, max_length=255, null=True)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('origine', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('depuis_millesime', models.IntegerField(blank=True, null=True)),
                ('jusque_millesime', models.IntegerField(blank=True, null=True)),
                ('fiabilite', models.CharField(blank=True, max_length=255, null=True)),
                ('doc', models.CharField(blank=True, max_length=255, null=True)),
                ('table_associee', models.CharField(max_length=255)),
                ('nature', models.CharField(blank=True, max_length=255, null=True)),
                ('modalites', models.ManyToManyField(to='dictionnaire.DescVariable')),
            ],
        ),
    ]
