from rest_framework import serializers
from .models import YoutubeVideo, VideoTag

class VideoTagSerializer (serializers.ModelSerializer):
    class Meta:
        model = VideoTag
        fields = ['tag']

class YoutubeVideoSerializer (serializers.ModelSerializer):
    tag = VideoTagSerializer(many=True,read_only=True)
    class Meta:
        model = YoutubeVideo
        fields = ['title', 'id', 'url','duration', 'view_count' , 'thumbnail', 'tag']