from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse
from slugify import slugify
# from django.utils.text import slugify

User = get_user_model()


class Post(models.Model):
    # поля таблицы
    # author = models.CharField(max_length=50, verbose_name='Автор')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=500, verbose_name='Текст объявления')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Опубликовано',
                                      editable=False)  # Параметр 'editable' отключает возможность для редактирования
    url_adders = models.CharField(max_length=150, verbose_name='Ссылка на сайт')
    image = models.ImageField(upload_to='posts/', null=True, verbose_name='Изображение')
    slug = models.SlugField(max_length=200, unique=True, editable=False, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('board:post_detail', kwargs={'slug': self.slug})

    class Meta:  # Настроечный класс
        # Имя таблицы в единственном числе
        verbose_name = 'Объявление'
        # Имя таблицы
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title

