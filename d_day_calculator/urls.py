from django.urls import path
from . import views

urlpatterns = [
    path('new', views.post_event),
    #path('events_list'),
    #path('event'),
]