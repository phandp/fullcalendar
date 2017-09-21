# Setting Up

create project with "django-admin startproject demo"

create app with "python manage.py startapp fullcalendar"

create superuser with "python manage.py createsuperuser"

create file in fullcalendar folder:  models.py, add CalendarEvent class 

create file in fullcalendar folder:  admin.py, register Model

run migrations (makemigrations and migrate)

enter admin and check is table is created, add some events with admin

create util.py with some helper functions such as event_to_json ....

check url localhost:8000/all_events/ : this should print a JSON object with all events in the database

# index page

create templates directory
create fullcalendar directory where you create index.html file which is an extension of base.html

make sure you the templatetags directory with the fullcalendar_tags.py inside

inside the index.html, the calendar will be shown inside the div tag with id="calendar". Styling was done locally to show the calendar in the middle of the page and limited in size.

in the base.html, CSS, js, jquery files for the Calendar are loaded.

# javascript

in the file fullcalendar_init.html, we find a javascript tag with the document ready function. Upon this, jQuery loads the calendar 

# status (inside calendar)

can display events
can move events
can modify events

cannot delete events
cannot have event changes persist
cannot create events inside calendar
cannot have modals 



