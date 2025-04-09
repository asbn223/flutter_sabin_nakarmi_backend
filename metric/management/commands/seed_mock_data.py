from django.core.management.base import BaseCommand
from main_utils.utils import create_mock_data

class Command(BaseCommand):
    help = "Seed mock data for development"

    def handle(self, *args, **kwargs):
        create_mock_data()
        self.stdout.write(self.style.SUCCESS("Mock data seeded successfully."))
