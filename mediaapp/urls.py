# mediaapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('media/<path:path>/', views.serve_media, name='serve_media'),
    path('upload/', views.upload_media, name='upload_media'),
    path('media-list/', views.media_list, name='media_list'),
    path('edit-media/<int:pk>/', views.edit_media, name='edit_media'),
    path('delete-media/<int:pk>/', views.delete_media, name='delete_media'),
]
