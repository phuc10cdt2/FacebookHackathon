from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required 	#for login required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from pocketlist.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def index(request):
	
	param = {}
	
	lists = List.objects.all()
	for l in lists:
		l.itemcount = Item.objects.filter(list = l).count()

	param['lists'] = lists
	
	return render_to_response(
		'index.html',
		param,
		context_instance=RequestContext(request)
	)

def view(request,listId):
	param={}
	param['list'] = List.objects.get(id = listId)
	items = Item.objects.filter(list_id= listId)
	paginator = Paginator(items, 5)
	
	try: page = int(request.GET.get("page", '1'))
	except ValueError: page = 1
	
	try:
		items = paginator.page(page)
	except (InvalidPage, EmptyPage):
		items = paginator.page(paginator.num_pages)
	
	param['items'] = items
	
	return render_to_response(
		'view.html',
		param,
		context_instance=RequestContext(request)
	)

def new(request):
	param = {}
	if request.method == 'GET':
		param['userId'] = request.GET['userId']
	if request.method == 'POST':
		newList = List()
		newList.title = request.POST['listName']
		newList.userId = request.POST['userId']
		title = newList.title
		des = request.POST['des']
		newList.description = des
		newList.status = 'public'
		newList.save()
<<<<<<< HEAD
		param['mes']= "<div class='alert alert-success'>A new list has been created successfully</div>"
		param['list'] = newList
		param['items'] = []
		return render_to_response('view.html',param,context_instance=RequestContext(request))
				
	return render_to_response('newlist.html',param,context_instance=RequestContext(request))

def addLink(request):
=======
	return render_to_response(
				'newlist.html',
				param,
				context_instance=RequestContext(request)
	)
#this function is not completed
def addLink(request, list_id):
>>>>>>> 2dcd222f08099673f2841c2a1ed4646732ad77d4
	param = {}
	print 'add link to list id = ' + list_id
	l = List.objects.filter(id = list_id)
	newLink = Item()
	newLink.link = ""
	newLink.list = l
	return render_to_response(
				'newlink.html',
				param,
				context_instance=RequestContext(request)
	)
def getList(request, list_id):
	param = {}
	list = List.objects.filter(id = list_id)
	return render_to_response(
				'list.html',
				param,
				context_instance=RequestContext(request)
	)
def deleteItem(request, itemId, listId):
	param = {}
	item = Item.objects.filter(id = itemId)
	item.delete()
	
	'''Hahaha
	'''
	param['list'] = List.objects.get(id = listId)
	items = Item.objects.filter(list_id= listId)
	paginator = Paginator(items, 5)
	
	try: page = int(request.GET.get("page", '1'))
	except ValueError: page = 1
	
	try:
		items = paginator.page(page)
	except (InvalidPage, EmptyPage):
		items = paginator.page(paginator.num_pages)
	
	param['items'] = items
	'''
	'''
	param['mes'] = "<div class='alert alert-success'>The item has been deleted successfully</div>"
	return render_to_response(
				'view.html',
				param,
				context_instance=RequestContext(request)
	)
def deleteList(request, listId):
	param = {}
	list = List.objects.filter(id = listId)
	items = Item.objects.filter(list = list)
	list.delete()
	items.delete()
	""""""
	lists = List.objects.all()
	for l in lists:
		l.itemcount = Item.objects.filter(list = l).count()
	param['lists'] = lists
	""""""
	param['mes'] = "<div class='alert alert-success'>The list has been deleted successfully</div>"
	return render_to_response(
				'index.html',
				param,
				context_instance=RequestContext(request)
	)