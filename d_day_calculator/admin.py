from django.contrib import admin
from .models import EventModel

# Register your models here.
@admin.register(EventModel)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ['id','event_name', 'event_date', 'event_comment']
    list_display_links = ['id', 'event_name']