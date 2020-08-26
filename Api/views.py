from rest_framework import filters
from .models import Video
from .serializers import VideoSerializer

# Rest FrameWork
from rest_framework.generics import ListAPIView


# Searching is implemented using DRF Filters
# DRF filter by default uses [icontains] and thus the search by default supports partial searches

class YoutubeItems(ListAPIView):
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ['channel_id', 'channel_title']
    ordering = ('-publishedDateTime')
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

