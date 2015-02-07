from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def fblogin(request, template="login_facebook.html"):
    return render(request, template)
