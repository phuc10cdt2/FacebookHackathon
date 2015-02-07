from django.conf import settings
from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns(
    '',
    url(r'^$', fblogin, name="fblogin"),

)
