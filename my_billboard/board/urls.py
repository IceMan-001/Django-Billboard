from django.urls import path
from board.views import index, about, contacts, add_post, post_list_in_table, post_list, post_detail, post_edit, \
    post_delete

app_name = 'board'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('post/add', add_post, name='add_post'),
    path('post/table/', post_list_in_table, name='post_list_in_table'),
    path('post/', post_list, name='post_list'),
    path('posts/<slug:slug>/', post_detail, name='post_detail'),
    path('posts/<int:pk>/edit/', post_edit, name='post_edit'),
    path('posts/<int:pk>/delete/', post_delete, name='post_delete'),
]
