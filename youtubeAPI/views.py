import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import VideoTag, YoutubeVideo
from .serializers import VideoTagSerializer, YoutubeVideoSerializer
from django.conf import settings
from isodate import parse_duration
import json
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .tasks import fetch_data
# Create your views here.

def index_view(request):
    """
    Render html page for youtube contents
    """
    data = YoutubeVideo.objects.all()
    if not data.exists():
        fetch_data()
    serializer = YoutubeVideoSerializer(data,many=True)

    context = {
        'videos' : serializer.data
    }
    
    return render(request, 'youtubeAPI/index.html', context)

class HomeView(generics.ListAPIView):
    """
    Get all youtube videos with video tags
    """
    queryset = YoutubeVideo.objects.all()
    serializer_class = YoutubeVideoSerializer
    pagination_class = PageNumberPagination
    
    def get(self,request):
        try:
            data = self.get_queryset()
            serializer = self.get_serializer(data,many=True)
            page = self.paginate_queryset(serializer.data)
            return self.get_paginated_response(page)
        except YoutubeVideo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PerformanceView(generics.ListAPIView):
    """
    Get all youtube videos with video tags sorted by video performance
    """
    queryset = YoutubeVideo.objects.all()
    serializer_class = YoutubeVideoSerializer
    pagination_class = PageNumberPagination
    
    def get(self,request):
        try:
            data = self.get_queryset().order_by('-view_count')
            serializer = self.get_serializer(data,many=True)
            page = self.paginate_queryset(serializer.data)
            return self.get_paginated_response(page)
        except YoutubeVideo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TagView(generics.ListAPIView):
    """
    Get filtered youtube videos based on tags
    """
    queryset = VideoTag.objects.all()
    serializer_class = YoutubeVideoSerializer
    pagination_class = PageNumberPagination
    
    def get(self,request):
        try:
            tags = VideoTag.objects.get(tag=request.GET.get('tag'))
            videos = tags.youtubeVideo.all()
            serializer = self.get_serializer(videos,many=True)
            page = self.paginate_queryset(serializer.data)
            return self.get_paginated_response(page)
        except YoutubeVideo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
