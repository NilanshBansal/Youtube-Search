from django.urls import path
from .views import YoutubeItems

urlpatterns = [
    path('', YoutubeItems.as_view())
]