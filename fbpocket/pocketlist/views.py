from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required 	#for login required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from pocketlist.models import *

def index(request):
	param = {}
	return render_to_response(
				'index.html',
				param,
				context_instance=RequestContext(request)
	)

def new(request):
	param = {}
	return render_to_response(
				'newlist.html',
				param,
				context_instance=RequestContext(request)
	)