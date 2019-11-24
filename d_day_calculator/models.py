from django.db import models
import datetime

# Create your models here.
# 로그인 연동 걸어야함
class EventModel(models.Model):
    event_name = models.CharField(max_length = 20)
    event_date = models.DateField()
    event_comment = models.CharField(max_length = 40)
    event_picture = models.ImageField(null = True, blank = True) #블랭크는 폼, 널은 디비
