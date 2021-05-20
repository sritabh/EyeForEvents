from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from .forms import EventForm,ParticipantForm
from .models import Event
from django import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    latest_events = Event.objects.order_by('-pub_date')[:10] #Top 10 Events in the DB
    context = {'latest_events': latest_events}
    return render(request, 'events/index.html', context)

#To register new events
@login_required(login_url='/user/login/')
def newEvent(request):
    return render(request, 'events/create_new.html')

@login_required(login_url='/user/login/')
def create_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST,request.FILES)
        # check whether it's valid:
        if form.is_valid():
            #form.save()
            ##Add the creator of the event to event details
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return HttpResponseRedirect('EventRegistered')

    return render(request, 'events/create_new.html', {'form': form,'error_message':"Something went wrong!"}) ##Incase above value is not returned keep the form values as it's


#SHow event details when requested
def detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return render(request, 'events/event_details.html', {'event': event,'event_by':event.created_by})


def successFull(request):
    return HttpResponse("Event Successfully Created")


@login_required(login_url='/user/login/')
def registerForEvent(request, event_id):
    #Register request contains Participant form
    if request.method == 'POST':
        user = request.user
        event = get_object_or_404(Event, pk=event_id)
        participant_details = {
            "email": user.email,
            "name": user.get_full_name(),
            "event": event
        }
        """
        Check if the user has already participated in the event or not
        """
        #If the participant with same event exists then don't allow user to participate again
        if event.participant_set.filter(email=user.email).count() >0:
            return render(request, 'events/event_details.html', {'event': event,'event_by':event.created_by,'msg':"You have already registered for this event!"})
        
        """
        Check if the event slot is available or not
        NOTE: 0 in event.max_capacity will denote that there's no caping of participants make sure it's exception
        """
        if event.participant_set.all().count()>=event.max_capacity and event.max_capacity !=0:
            return render(request, 'events/event_details.html', {'event': event,'event_by':event.created_by,'msg':"No slot/seat is available, event is full!"})
        user.participated_in.add(event)
        #Participant form is invisible to the user will be filled automatically by fetching whether the user is logged in or not
        form = ParticipantForm(data=participant_details) 
        
        if form.is_valid():
            form.save()
            event.save()
            return render(request, 'events/error.html', {'form': form,'msg':"Successfully registered"})
    return render(request, 'events/error.html', {'form': form,'msg':"Something went wrong!"})
