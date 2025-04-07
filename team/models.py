import uuid

from django.db import models

# Create your models here.
class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('CEO', 'Chief Executive Officer'),
        ('CTO', 'Chief Technology Officer'),
        ('PM', 'Project Manager'),
        ('DEV', 'Developer'),
        ('DS', 'Data Scientist'),
        ('UX', 'UX Designer'),
        ('QA', 'Quality Assurance'),
        ('HR', 'Human Resources'),
        ('MK', 'Marketing'),
        ('SALES', 'Sales'),
        ('SUPPORT', 'Customer Support'),
        ('OTHER', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    email = models.EmailField()
    avatar_url = models.URLField()

