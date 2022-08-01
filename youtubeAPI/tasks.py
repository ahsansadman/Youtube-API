import requests
from .models import VideoTag, YoutubeVideo
from .serializers import VideoTagSerializer, YoutubeVideoSerializer
from django.conf import settings
from isodate import parse_duration
from .models import YoutubeVideo

def fetch_data():
    """
    fetch all video information from youtube api and update the database 
    """
    video_ids = []
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    videos = YoutubeVideo.objects.all()
    
    if videos.exists():
        video_ids = list(YoutubeVideo.objects.values_list('id', flat = True))

        
    else:
        search_params = {
            'part' : 'snippet',
            'channelId' : 'UC8butISFwT-Wl7EV0hUK0BQ',
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 50,
            'type' : 'video'
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['items']
        
        for result in results:
            video_ids.append(result['id']['videoId'])
        
    ############################

    video_params = {
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'part' : 'snippet,contentDetails,statistics',
        'id' : ','.join(video_ids),
        'maxResults' : 50
    }
    r = requests.get(video_url, params=video_params)

    results = r.json()['items']
    
    for result in results:
        video_data, created = YoutubeVideo.objects.update_or_create(id=result['id'], defaults={
            'title' : result['snippet']['title'],
            'view_count' : int(result['statistics']['viewCount']),
            'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
            'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            'thumbnail' : result['snippet']['thumbnails']['high']['url'],
        })
        
        if 'tags' in result['snippet']:
            tags = result['snippet']['tags']
            for tag in tags:
                tag_data,created = VideoTag.objects.get_or_create(tag=tag)
                # if created:
                video_data.tag.add(tag_data)
                video_data.save()  

            # videos.append(json.dumps(video_data))
    # print(videos)
