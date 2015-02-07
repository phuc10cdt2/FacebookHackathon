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
	return render_to_response(
				'index.html',
				param,
				context_instance=RequestContext(request)
	)

def new(request):
	param = {}
	if request.method == 'POST':
		print 'new list request'
		newList = List()
		newList.title = request.POST['listName']
		title = newList.title
		print "list title = " + title
		des = request.POST['des']
		newList.description = des
		print "list des = " +  des
		newList.status = 'public'
		newList.save()
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
def getList(request, list_id):
	param = {}
	print 'get list with id = ' + list_id
	list = List.objects.filter(id = list_id)
	print list
	return render_to_response(
				'list.html',
				param,
				context_instance=RequestContext(request)
	)