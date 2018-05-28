from django.urls import path
from bookmark.views import *


app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListView.as_view(), name='index'),
    path('create/', BookmarkCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]
