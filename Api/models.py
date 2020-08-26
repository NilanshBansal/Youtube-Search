from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length=300, blank=True, null=True)
    title = models.CharField(max_length=700, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    publishedDateTime = models.DateTimeField()
    thumbnailsUrls = models.URLField()
    channel_id = models.CharField(max_length=500, blank=True, null=True)
    channel_title = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

