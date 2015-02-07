from django.conf import settings
from django.conf.urls import patterns, url
from fbpocket.fblogin import views

urlpatterns = patterns(
    '',
    url(r'^$', views.fblogin, name="fblogin"),
)
