from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'courseswebsite.users'

    def ready(self):
        from . import signals  # noqa: F401
