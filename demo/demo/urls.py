from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'fullcalendar.views.index', name='index'),
    url(r'^all_events/', 'fullcalendar.views.all_events', name='all_events'),
	#url(r'^$', include('fullcalendar.urls')),
    url(r'^admin/', admin.site.urls),
]
