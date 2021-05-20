import uuid
from django.db import models
from django.utils import timezone
import datetime
from django.conf import settings

#Event Database Model
class Event(models.Model):
    #FIX-ME: Change default values of parameters
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #unique id to differentiate between events
    name = models.CharField("name",max_length=200) #Event name
    description = models.CharField("description",max_length=2000,default="") #Event description
    max_capacity = models.PositiveSmallIntegerField("max_capacity",default=0) #0 for not applicable and >0 if there's a capacity
    location = models.CharField(max_length=500,default="")
    contact_number = models.PositiveSmallIntegerField("contact_number",default=0)
    alt_contact_number = models.PositiveSmallIntegerField("alt_contact_number",default=0)
    contact_email = models.EmailField(max_length=254)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,related_name="created_by") #One to Many relationship 
    participated_in = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="participated_in") #One to Many relationship showing user participated in events relation
    event_image = models.ImageField(upload_to='events/'+str(uuid.uuid4()),blank=True,null=True) #Image for the event not needed but would be better if we get one
    last_date = models.DateTimeField(default = timezone.now()) #Last date till the event registeration is available
    event_date = models.DateTimeField(default = timezone.now()) #Date of the event
    pub_date = models.DateTimeField('Created On',auto_now_add=True) #Will be used to check how old is the posted events
    def __str__(self):
        return self.name #For Debugging purpose

class Participant(models.Model):
    """
    Each participant is related to a particular event
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE,blank=True) #One to Many relationship - many participant can participate in one event
    name = models.CharField(max_length=200,default=None)
    email = models.EmailField(max_length=254,default=None)
    def __str__(self):
        return (self.email)
    #FIX-ME: Should store user_id too so that it can be verified easi

