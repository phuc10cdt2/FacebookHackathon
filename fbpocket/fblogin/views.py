from django.shortcuts import render

# Create your views here.


def login_facebook(request, template="login_facebook.html"):
    return render(request, template)
