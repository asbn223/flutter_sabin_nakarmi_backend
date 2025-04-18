# Generated by Django 5.2 on 2025-04-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metric', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertracking',
            name='from_lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='ordertracking',
            name='from_lon',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='ordertracking',
            name='to_lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='ordertracking',
            name='to_lon',
            field=models.FloatField(default=0.0),
        ),
    ]
