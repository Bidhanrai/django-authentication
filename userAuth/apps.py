from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'userAuth'

    def ready(self):
        import userAuth.signals
