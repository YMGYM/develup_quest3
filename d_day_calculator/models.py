from django.db import models

# Create your models here.
class EventModel(models.Model):
    event_name = models.CharField(max_length = 20)
    event_date = models.DateField()
    event_comment = models.CharField(max_length = 40)
    event_picture = models.ImageField()