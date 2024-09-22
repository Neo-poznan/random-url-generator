from django.apps import AppConfig


class HashgenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hashgen'

    def ready(self) -> None:
        import threading
        from .url_generating import start_generating
        threading.Thread(target=start_generating).start()
        
