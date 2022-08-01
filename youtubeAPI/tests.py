from django.test import TestCase
from django.test import Client
from rest_framework.test import APITestCase
from .models import VideoTag, YoutubeVideo
from django.urls import reverse
import json

# Create your tests here.


class GetYoutubeVideoTest(APITestCase):
    """
    Test module for getting list of youtube videos
    """
    def setUp(self):

        test_tag = {
            "tag": "html",
        }

        test_video = {
            "title": "What are Microservices?",
            "id": "j3XufmvEMiM",
            "url": "https://www.youtube.com/watch?v=j3XufmvEMiM",
            "duration": 3,
            "view_count": 225813,
            "thumbnail": "https://i.ytimg.com/vi/j3XufmvEMiM/hqdefault.jpg"
        }

        self.tag = VideoTag.objects.create(**test_tag)
        self.video1 = YoutubeVideo.objects.create(**test_video)
        self.video1.tag.add(self.tag)

        self.test_data = [
            {  
                "title": "What are Microservices?",
                "id": "j3XufmvEMiM",
                "url": "https://www.youtube.com/watch?v=j3XufmvEMiM",
                "duration": 3,
                "view_count": 225813,
                "thumbnail": "https://i.ytimg.com/vi/j3XufmvEMiM/hqdefault.jpg",
                "tag": [
                    {
                        "tag": "html"
                    },
                ]
            }
        ]

    def test_get_all_videos(self):

        response = self.client.get(
            reverse('home_view')
        )

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(json.loads(response.content)["results"], self.test_data)


class FilterTest(APITestCase):
    """
    Test module for getting filtered videos based on tags or performance
    """
    
    def setUp(self):

        test_tag = {
            "tag": "html",
        }

        test_video1 = {
            "title": "What are Microservices?",
            "id": "j3XufmvEMiM",
            "url": "https://www.youtube.com/watch?v=j3XufmvEMiM",
            "duration": 3,
            "view_count": 225813,
            "thumbnail": "https://i.ytimg.com/vi/j3XufmvEMiM/hqdefault.jpg"
        }

        test_video2 = {
            "title": "Async + Await in JavaScript, talk from Wes Bos",
            "id": "DwQJ_NPQWWo",
            "url": "https://www.youtube.com/watch?v=DwQJ_NPQWWo",
            "duration": 15,
            "view_count": 104514,
            "thumbnail": "https://i.ytimg.com/vi/DwQJ_NPQWWo/hqdefault.jpg",
            
        }
        self.tag = VideoTag.objects.create(**test_tag)
        self.video1 = YoutubeVideo.objects.create(**test_video1)
        self.video1.tag.add(self.tag)
        
        self.video2 = YoutubeVideo.objects.create(**test_video2)

        self.test_data1 = [
            {  
                "title": "What are Microservices?",
                "id": "j3XufmvEMiM",
                "url": "https://www.youtube.com/watch?v=j3XufmvEMiM",
                "duration": 3,
                "view_count": 225813,
                "thumbnail": "https://i.ytimg.com/vi/j3XufmvEMiM/hqdefault.jpg",
                "tag": [
                    {
                        "tag": "html"
                    },
                ]
            }
        ]
        
        self.test_data2 = [
            {  
                "title": "What are Microservices?",
                "id": "j3XufmvEMiM",
                "url": "https://www.youtube.com/watch?v=j3XufmvEMiM",
                "duration": 3,
                "view_count": 225813,
                "thumbnail": "https://i.ytimg.com/vi/j3XufmvEMiM/hqdefault.jpg",
                "tag": [
                    {
                        "tag": "html"
                    },
                ]
            },
            
            {
            "title": "Async + Await in JavaScript, talk from Wes Bos",
            "id": "DwQJ_NPQWWo",
            "url": "https://www.youtube.com/watch?v=DwQJ_NPQWWo",
            "duration": 15,
            "view_count": 104514,
            "thumbnail": "https://i.ytimg.com/vi/DwQJ_NPQWWo/hqdefault.jpg",
            "tag": []     
        }
        ]
        
        
        
    def test_filter_by_tag(self):

        response = self.client.get('%s?tag=%s' % (reverse('tag_view'), self.tag.tag))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(json.loads(response.content)["results"], self.test_data1)
    
        
    def test_filter_by_performance(self):

        response = self.client.get(reverse('performance_view'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(json.loads(response.content)["results"], self.test_data2)
