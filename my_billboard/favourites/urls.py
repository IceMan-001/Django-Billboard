from django.urls import path
from .views import favourites_detail

urlpatterns = [
    path('detail/', favourites_detail, name="favourites_detail"),
]
