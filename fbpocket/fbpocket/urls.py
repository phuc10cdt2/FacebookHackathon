from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from pocketlist import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^$', views.index),
	(r'^new/', views.new),
	(r'^add/', views.addLink),
)
