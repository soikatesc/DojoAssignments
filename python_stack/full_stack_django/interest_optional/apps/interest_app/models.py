from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=255)
	user_interest = models.ManyToManyField('self')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Interest(models.Model):
	interest = models.CharField(max_length=255)
	# user = models.ForeignKey(User, related_name='interests')
	interests = models.ManyToManyField(User,related_name="interest")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


