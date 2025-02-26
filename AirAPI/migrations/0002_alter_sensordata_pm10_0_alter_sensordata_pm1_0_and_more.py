# Generated by Django 5.1.6 on 2025-02-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='pm10_0',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='pm1_0',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='pm2_5',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
