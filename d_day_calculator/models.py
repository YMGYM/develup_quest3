from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
# 로그인 연동 걸어야함
class EventModel(models.Model):
    event_name = models.CharField(max_length = 20)
    is_main = models.BooleanField(default = False)
    start_date = models.DateField()
    event_date = models.DateField()
    event_comment = models.CharField(max_length = 40)
    event_picture = models.ImageField(null = True, blank = True) #블랭크는 폼, 널은 디비
    
    user = models.ForeignKey(User, on_delete = models.CASCADE)

