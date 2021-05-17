from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from .forms import EventForm
from .models import Event

# Create your views here.
def index(request):
    latest_events = Event.objects.order_by('-pub_date')[:10] #Top 10 Questions
    context = {'latest_events': latest_events}
    return render(request, 'events/index.html', context)

#To register new events
def newEvent(request):
    #
    return render(request, 'events/create_new.html')

def create_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('EventRegistered')

    return render(request, 'events/create_new.html', {'form': form,'error_message':"Something went wrong!"}) ##Incase above value is not returned keep the form values as it's


#SHow event details when requested
def detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return render(request, 'events/event_details.html', {'event': event})


def successFull(request):
    return HttpResponse("Event Successfully Registerd")