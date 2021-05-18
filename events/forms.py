from django import forms
from .models import Event
from .models import Participant

##Creating a model form
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = "__all__"
