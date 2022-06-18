from django.db import DJANGO_VERSION_PICKLE_KEY

from django.urls import URLPattern, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import PostListView, PostDetailView, post_create, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', post_create, name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search/',views.search,name='search1'),
    path('api/post/',views.PostView.as_view(),name='apipost'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)