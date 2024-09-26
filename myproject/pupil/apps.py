from django.apps import AppConfig


class PupilConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pupil'

def ready(self):
    import pupil.signals
