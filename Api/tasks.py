from datetime import datetime, timedelta
from celery.task.schedules import crontab
from celery.decorators import periodic_task

# Google API
from apiclient.discovery import build
import apiclient
from Api.models import Video
from YoutubeFetch import settings


"""
Periodic task to fetch data from Youtube Api and store in the DB
"""

# runs after every 5 minutes
@periodic_task(run_every=crontab(minute='*/2'))
def fetch_youtube_data():
    code = 'api.call_youtube_api'    # a unique code
    apikeys = settings.GOOGLE_API_KEYS
    time_now = datetime.now()
    last_request_time = time_now - timedelta(minutes=5)

    # A variable to check if a valid api key exists or not
    valid = False

    for apikey in apikeys:
        try:
            youtube = build("youtube", "v3", developerKey=apikey, cache_discovery=False)
            req = youtube.search().list(q="cricket", part="snippet", order="date", maxResults=50,
                                        publishedAfter=(last_request_time.replace(microsecond=0).isoformat()+'Z'))
            res = req.execute()
            valid = True
        except apiclient.errors.HttpError as err:
            code = err.resp.status
            if not code in [400, 403]:
                break

        if valid:
            break

    if valid:
        # Creating Video Entry in the Database
        for item in res['items']:
            video_id = item['id']['videoId']
            published_date_time = item['snippet']['publishedAt']
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnails_urls = item['snippet']['thumbnails']['default']['url']
            channel_id = item['snippet']['channelId']
            channel_title = item['snippet']['channelTitle']
            Video.objects.create(
                video_id=video_id,
                title=title,
                description=description,
                channel_id=channel_id,
                channel_title=channel_title,
                publishedDateTime=published_date_time,
                thumbnailsUrls=thumbnails_urls,
            )
