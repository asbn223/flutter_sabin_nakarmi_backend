from django.apps import AppConfig


class MetricConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'metric'

    def ready(self):
        from main_utils.utils import create_mock_data
        create_mock_data()