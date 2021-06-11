from .views import SpitefulReader
from django.urls import path


urlpatterns = [
    path("", SpitefulReader.as_view())
]
