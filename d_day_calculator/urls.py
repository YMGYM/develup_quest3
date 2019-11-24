from django.urls import path
from . import views

urlpatterns = [
    path('new', views.post_event),
    path('event', views.view_events, name = "view_events"),
    #path('events_list'),
    #path('event'),
]