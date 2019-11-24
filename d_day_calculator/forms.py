from django import forms
from .models import EventModel

class PostEventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ('event_name', 'event_date', 'start_date','event_comment', 'event_picture')
        