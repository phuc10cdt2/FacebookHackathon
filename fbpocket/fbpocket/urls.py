from django.conf.urls import patterns, include, url
from pocketlist import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', views.index),
    (r'^fblogin/', include('fblogin.urls')),
	(r'^admin/', include(admin.site.urls)),
	(r'^$', views.index),
	(r'^new/', views.new),
	(r'^add/', views.addLink),
)
