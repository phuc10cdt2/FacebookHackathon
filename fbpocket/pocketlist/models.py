from django.db import models

'''	
class User(models.Model):
	id = models.IntegerField(primary_key=True, null=False)
	name = models.CharField(max_length=64, null=True)
'''
class List(models.Model):
	id = models.IntegerField(primary_key=True, null=False)
	title = models.CharField(max_length=64, null=True)
	description = models.CharField(max_length=500, null=True)
	status = models.CharField(max_length=10, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userId = models.CharField(max_length=100, null=True)
	
	def __str__(self):
		return str(self.title)

class Item(models.Model):
	id = models.IntegerField(primary_key=True, null=False)
	link = models.CharField(max_length=500, null=True)
	fbId = models.CharField(max_length=500, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	list = models.ForeignKey(List, null=False)
	
	def __str__(self):
		return str(self.id)
