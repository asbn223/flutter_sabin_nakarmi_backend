# Generated by Django 5.2 on 2025-04-08 07:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('CEO', 'Chief Executive Officer'), ('CTO', 'Chief Technology Officer'), ('PM', 'Project Manager'), ('DEV', 'Developer'), ('DS', 'Data Scientist'), ('UX', 'UX Designer'), ('QA', 'Quality Assurance'), ('HR', 'Human Resources'), ('MK', 'Marketing'), ('SALES', 'Sales'), ('SUPPORT', 'Customer Support'), ('OTHER', 'Other')], max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('avatar_url', models.URLField()),
            ],
        ),
    ]
