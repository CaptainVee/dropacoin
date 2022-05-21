from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
path('new/', PostCreateView.as_view(), name='post-create'),
path('<int:pk>/detail/', PostDetailView.as_view(), name='post-detail'),
path('<str:username>/', UserPostListView.as_view(), name='user-post'),
path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

 ]