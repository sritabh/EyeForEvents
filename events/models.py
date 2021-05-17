from django.db import models
from django.utils import timezone
import datetime

#Event Database Model
class Event(models.Model):
    event_name = models.CharField("event_name",max_length=200)
    event_description = models.CharField("event_description",max_length=2000,default="")
    pub_date = models.DateTimeField('Created On',auto_now_add=True) #Will be used to check how old is the posted events
    def __str__(self):
        return self.event_name #For Debugging purpose