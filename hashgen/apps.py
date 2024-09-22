from django.apps import AppConfig


class HashgenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hashgen'

    def ready(self) -> None:
        import threading
        from .url_generating import url_generation_loop
        threading.Thread(target=url_generation_loop).start()
        
