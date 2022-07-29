from django.urls import path
from .views import DestListView
urlpatterns = [
    path('',DestListView.as_view(),name='dest-list')
]