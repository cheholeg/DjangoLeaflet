# Generated by Django 4.0.4 on 2022-06-15 11:02

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0006_alter_route_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='location',
            field=django.contrib.gis.db.models.fields.MultiLineStringField(null=True, srid=4326),
        ),
    ]