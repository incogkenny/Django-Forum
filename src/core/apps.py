# Import the AppConfig class from Django's apps module
from django.apps import AppConfig


# Define a configuration class for the 'core' app
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
