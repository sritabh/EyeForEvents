![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# EyeForEvents
 EyeForEvent is a web app which gives a convenient way to manage events and participants.
 EyeForEvent makes it easy for anyone to find events of their choice and track the records of events they participated in, it also allows the user to create their own event and invite others to participate in.
 The user who created the event can decide the maximum capacity of the event and can see the list of participants who has registered for the event.
 While creating any event, the user can decide to keep the last date for registeration, after which the registeration will no longer be accepted.
 Users can now keep an EYE on the events around them easily.
 <br>
 <br>
## Team members
1. <a href="https://github.com/anandalisha">Alisha Anand</a>
2. <a href="https://github.com/anusham14">Anusha Maiti</a>
3. <a href="https://github.com/SobyDamn">Sritabh Priyadarshi</a>
## Team Id
BFH/recFqPDxQAhif8mzp/2021
## Link to product walkthrough

<a href="https://www.loom.com/share/9e93165490214ef5981990f0992fe8ae">Walkthrough video</a>
<br>

## How it Works ?
1. The user creates the account registering using emails.
2. The who is authenticated(registered) can create events providing details about the event
3. The data about the event and the details about the user who created it is saved into the database model in SQL Lite DB
4. The meaningful detail of the participant(user who is trying to register for the event) is also stored in participant model and is related to event model by one-to-many relation.
5. The User model(Default in django) is related to event by many-to-many relation allowing the user to act as both participant and creator for the events.
6. The details stored in the DB model is then retrived by and displayed to the user accessing, as per user demands and accessibility.

## Libraries used
django==3.2.3
<br>
django-storages[azure]>=1.9.1
<br>
Pillow>=8.1.0

## How to configure
<dl>NOTE: Deployable file are available in <a href="https://github.com/SobyDamn/EyeForEvents/tree/deployable">deployable</a> branch, the files can be used to deploy django app on azure web app service.
</dl>
<dl>
    <dt>Setting things up!</dt>
    <dd>
        <dl>
            <dt>1. Set up the azure web service and connect the github repository for deploying the codes</dt>
            <dt>2. Set up <a href="https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction">Azure Blob Storage</a> containers with name <i>media</i> and <i>static</i> for storing static and media files</dt>
            Here we are storing all the media file uploaded by the users for creating events in the <i>media</i> container and styling files required in <i>static</i> container.
            <dt>3. Set up environment variables in the web app you created for <b><i>SECRET_KEY</i></b> which is django secret key and <b><i>AZURE_STORAGE_KEY</i></b> which is your storage access key.</dt>
            <dt>4.Change the app app names of the storage and the web app created in settings.py as per your condition.</dt>
        </dl>
    </dd>
    <dt>Deploying</dt>
    <dd>
        Once the file is connected to the azure app, just hit refresh or push any commit which will trigger the web app to restart, once successfully deployed it can be viewed by the browsing link available in the azure web app portal.
    </dd>
</dl>

## How to Run (Locally)
1. Clone the master branch in your system.
2. Make sure you have the libraries mentioned above installed in your system, use pip if you don't have the required libraries to install the packages.
3. run the command
```
python manage.py runserver
```
4. The web app will be visible locally 
