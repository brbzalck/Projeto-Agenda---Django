from django.apps import AppConfig


class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # name do app é usado em settings para fins de rastreamento
    name = 'contact'
