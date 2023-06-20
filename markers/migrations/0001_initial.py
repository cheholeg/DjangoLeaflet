# Generated by Django 4.0.4 on 2022-06-15 09:52

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.spatial


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', location_field.models.spatial.LocationField(default=django.contrib.gis.geos.point.Point(1.0, 1.0), srid=4326)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('amenity', models.CharField(default='Сражение', editable=False, max_length=255)),
                ('amenity1', models.CharField(default='battle', editable=False, max_length=255)),
                ('audio', models.CharField(blank=True, default='', max_length=255)),
                ('photo', models.CharField(blank=True, default='', max_length=255)),
                ('video', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Municipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('amenity', models.CharField(default='Муниципальный район', editable=False, max_length=255)),
                ('amenity1', models.CharField(default='Municipal', editable=False, max_length=255)),
                ('area', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', location_field.models.spatial.LocationField(default=django.contrib.gis.geos.point.Point(1.0, 1.0), srid=4326)),
                ('period', models.CharField(blank=True, max_length=255, null=True)),
                ('place', models.CharField(blank=True, max_length=255, null=True)),
                ('size', models.CharField(blank=True, max_length=255, null=True)),
                ('commander', models.CharField(blank=True, max_length=255, null=True)),
                ('amenity', models.CharField(default='Полк', editable=False, max_length=255)),
                ('amenity1', models.CharField(default='regiment', editable=False, max_length=255)),
                ('audio', models.CharField(blank=True, default='', max_length=255)),
                ('photo', models.CharField(blank=True, default='', max_length=255)),
                ('video', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Toponym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', location_field.models.spatial.LocationField(default=django.contrib.gis.geos.point.Point(1.0, 1.0), srid=4326)),
                ('place', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('audio', models.CharField(blank=True, default='', max_length=255)),
                ('photo', models.CharField(blank=True, default='', max_length=255)),
                ('video', models.CharField(blank=True, default='', max_length=255)),
                ('amenity', models.CharField(default='Топоним', editable=False, max_length=255)),
                ('amenity1', models.CharField(default='toponym', editable=False, max_length=255)),
                ('municipals', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='markers.municipal')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.MultiLineStringField(null=True, srid=4326)),
                ('length', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('amenity', models.CharField(default='Маршрут', editable=False, max_length=255)),
                ('amenity1', models.CharField(default='route', editable=False, max_length=255)),
                ('audio', models.CharField(blank=True, default='', max_length=255)),
                ('photo', models.CharField(blank=True, default='', max_length=255)),
                ('video', models.CharField(blank=True, default='', max_length=255)),
                ('regiment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='markers.regiment')),
            ],
        ),
        migrations.CreateModel(
            name='Monument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', location_field.models.spatial.LocationField(default=django.contrib.gis.geos.point.Point(1.0, 1.0), srid=4326)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('architect', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('amenity', models.CharField(default='Памятник', editable=False, max_length=255)),
                ('amenity1', models.CharField(default='monument', editable=False, max_length=255)),
                ('audio', models.CharField(blank=True, default='', max_length=255)),
                ('photo', models.CharField(blank=True, default='', max_length=255)),
                ('video', models.CharField(blank=True, default='', max_length=255)),
                ('municipals', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='markers.municipal')),
            ],
        ),
        migrations.CreateModel(
            name='LineToponym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.MultiLineStringField(null=True, srid=4326)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('audio', models.CharField(blank=True, default='', max_length=255)),
                ('photo', models.CharField(blank=True, default='', max_length=255)),
                ('video', models.CharField(blank=True, default='', max_length=255)),
                ('amenity', models.CharField(default='Топоним', editable=False, max_length=255)),
                ('amenity1', models.CharField(default='toponym', editable=False, max_length=255)),
                ('municipals', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='markers.municipal')),
                ('toponyms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='markers.toponym')),
            ],
        ),
        migrations.CreateModel(
            name='Fort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', location_field.models.spatial.LocationField(default=django.contrib.gis.geos.point.Point(1.0, 1.0), srid=4326)),
                ('latitude', models.CharField(editable=False, max_length=255, null=True)),
                ('longitude', models.CharField(editable=False, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('amenity', models.CharField(default='fort', editable=False, max_length=255)),
                ('audio', models.CharField(blank=True, default='', max_length=255)),
                ('photo', models.CharField(blank=True, default='', max_length=255)),
                ('video', models.CharField(blank=True, default='', max_length=255)),
                ('battles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='markers.battle')),
            ],
        ),
        migrations.AddField(
            model_name='battle',
            name='regiments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='markers.regiment'),
        ),
    ]