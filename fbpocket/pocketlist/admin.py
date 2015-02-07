from django.contrib.admin import AdminSite
from django.contrib import admin

from pocketlist.models import *


admin.site.register(List)
admin.site.register(Item)

