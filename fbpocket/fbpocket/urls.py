from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
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
	(r'^view/(?P<listId>\d+)/$', views.view),
	(r'^deleteItem/(?P<itemId>\d+)/(?P<listId>\d+)/$', views.deleteItem),
	(r'^deleteList/(?P<listId>\d+)/$', views.deleteList),
	(r'^add/(?P<list_id>\d+)/$', views.addLink),
	(r'^list/(?P<list_id>\d+)/$', views.getList),
)
