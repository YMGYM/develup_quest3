from django.urls import path
from . import views

app_name="event"
urlpatterns = [
    path('event', views.view_events, name = "view_events"),
    #path('events_list'),
    #path('event'),
]