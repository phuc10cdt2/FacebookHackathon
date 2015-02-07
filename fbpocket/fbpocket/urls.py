from django.conf.urls import patterns, include, url
from pocketlist import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index),
    url(r'^fblogin/', include('fblogin.urls')),
)
