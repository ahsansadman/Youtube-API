from django.contrib import admin
from .models import YoutubeVideo, VideoTag
# Register your models here.

admin.site.register(YoutubeVideo)
admin.site.register(VideoTag)