# Generated by Django 4.0.4 on 2022-06-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0004_fort_amenity1_alter_fort_amenity'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='kuda',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='otkuda',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
