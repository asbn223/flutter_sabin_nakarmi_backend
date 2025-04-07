# Generated by Django 5.2 on 2025-04-07 06:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('variants', models.JSONField(default=dict)),
                ('budget_info', models.JSONField(default=dict)),
                ('specifications', models.JSONField(default=dict)),
                ('materials', models.TextField()),
                ('images', models.JSONField(default=list)),
            ],
        ),
    ]
