from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Client(models.Model):
	business_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	notes = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# objects = UserManager()

class Project(models.Model):
	project_name = models.CharField(max_length=255)
	notes = models.TextField()
	client = models.ForeignKey(Client, related_name="projects")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
