from django.db import models
from django.contrib.auth import get_user_model
from board.models import Post

User = get_user_model()


class FavouritesUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class FavouritesItem(models.Model):
    favourites = models.ForeignKey(FavouritesUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
