from django.db import DJANGO_VERSION_PICKLE_KEY

from django.urls import URLPattern, path

from . import views
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]