from django.apps import AppConfig


class YoutubeapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'youtubeAPI'
    
    def ready(self):
        from . import updater
        updater.start()
