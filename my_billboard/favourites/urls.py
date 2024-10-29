from django.urls import path
from .views import favourites_detail


app_name = 'favourites'

urlpatterns = [
    path('detail/', favourites_detail, name="favourites_detail"),
]
