from django import forms
from .models import Event

##Creating a model form
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
