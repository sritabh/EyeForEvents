from django import forms
from .models import Event
from .models import Participant

##Creating a model form
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'max_capacity','location','contact_number','alt_contact_number','contact_email']


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = "__all__"
