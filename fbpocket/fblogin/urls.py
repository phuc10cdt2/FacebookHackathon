from django.conf import settings
from django.conf.urls import patterns, url
# from fbpocket.fblogin import views
from .views import *

urlpatterns = patterns(
    '',
    url(r'^$', fblogin, name="fblogin"),

)
