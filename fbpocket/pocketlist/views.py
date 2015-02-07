from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 	#for login required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from pocketlist.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import simplejson, json
import django.utils.simplejson as json
from pocketlist.models import List
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson

def index(request):
	param = {}
	lists = List.objects.filter(userId = 88).order_by("-created_at").order_by('-status')
	for l in lists:
		l.itemcount = Item.objects.filter(list = l).count()
		l.descriptionShort = l.description[:118]
	paginator = Paginator(lists, 7)
	
	try: page = int(request.GET.get("page", '1'))
	except ValueError: page = 1
	
	try:
		lists = paginator.page(page)
	except (InvalidPage, EmptyPage):
		lists = paginator.page(paginator.num_pages)
		
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
	for t in items:
		t.date = (t.created_at).date()
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

def update(request,listId):
	param = {}
	list = List.objects.get(id = listId)
	param['list'] = list
	if request.method == 'POST':
		list.title = request.POST['listName']
		list.description = request.POST['des']
		list.status = request.POST['status']
		list.save()
		param['mes']= "<div class='alert alert-success'>A new list has been updated successfully</div>"
		param['list'] = list
		return view(request,listId)
				
	return render_to_response('updatelist.html',param,context_instance=RequestContext(request))	
	
def new(request):
	param = {}
	if request.method == 'GET':
		param['userId'] = request.GET['userId']
	if request.method == 'POST':
		newList = List()
		newList.title = request.POST['listName']
		newList.userId = request.POST['userId']
		#print userId
		#print "-----------------"
		title = newList.title
		des = request.POST['des']
		newList.description = des
		newList.status = request.POST['status']
		newList.save()
		param['mes']= "<div class='alert alert-success'>A new list has been created successfully</div>"
		param['list'] = newList
		param['items'] = []
		return render_to_response('view.html',param,context_instance=RequestContext(request))
				
	return render_to_response('newlist.html',param,context_instance=RequestContext(request))



def edit(request, list_id):
	list = get_object_or_404(List, pk=list_id)
	param = {}
	param['list'] = list

	if request.method == 'GET':
		param['userId'] = request.GET['userId']


	if request.method == 'POST':
		list.title = request.POST['listName']
		list.description = request.POST['des']
		list.status = 'public'
		list.save()
		param['mes']= "<div class='alert alert-success'>The list has been updated successfully</div>"
		param['list'] = list
		param['items'] = []
		return render_to_response('view.html', param, context_instance=RequestContext(request))
	else:
		return render_to_response('editlist.html',param,context_instance=RequestContext(request))

@csrf_exempt
def addLink(request,listId):
	param = {}
	link = request.GET.get("link", 'Error')
	elements = link.split("/")
	list = List.objects.get(id = listId)
	for i in range(len(elements)-1,0,-1):
		if len(elements[i])==16:
			id = elements[i]
			break
	newItem = Item(list = list, link = link, fbId = id)
	
	newItem.save()
	param['debug'] = newItem.link
	return HttpResponse(1, content_type="application/json")
	
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
def api_list(request,userId):
	param = {}
	lists = List.objects.filter(userId = "88").filter(status='public')
	data = []
	for l in lists:
		line = {}
		line['id'] = l.id
		line['title'] = l.title
		data.append(line)
	returnJson = json.dumps(data)
	param['debug'] = returnJson
	return HttpResponse(json.dumps(returnJson), content_type="application/json")