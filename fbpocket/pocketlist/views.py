from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required 	#for login required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from pocketlist.models import *

def index(request):
	param = {}
	lists = List.objects.all()
	param['lists'] = lists
	for l in lists:
		l.items = Item.objects.filter(list=l)
		l.itemcount = len(l.items)
		l.items[:3]
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

def addLink(request):
	param = {}
	return render_to_response(
				'newlink.html',
				param,
				context_instance=RequestContext(request)
	)