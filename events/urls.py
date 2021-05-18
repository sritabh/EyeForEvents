from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.newEvent, name='create'),
    path('CreateEvent', views.create_event, name='create_event'), #Store event details to db
    # Ex - /events/EventRegistered
    path('EventRegistered',views.successFull,name="event_created_successfully"),
    #Example - /events/5
    path('<uuid:event_id>/', views.detail, name='detail'),
    path('<uuid:event_id>/Register', views.registerForEvent, name='Register'),
]