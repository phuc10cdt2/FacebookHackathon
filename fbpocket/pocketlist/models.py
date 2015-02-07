from django.db import models


class List(models.Model):
	id = models.IntegerField(primary_key=True, null=False)
	title = models.CharField(max_length=64, null=True)
	description = models.CharField(max_length=500, null=True)
	status = models.CharField(max_length=10, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return str(self.title)

class Item(models.Model):
	id = models.IntegerField(primary_key=True, null=False)
	link = models.CharField(max_length=500, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return str(self.id)
		
