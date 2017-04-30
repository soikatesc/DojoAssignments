from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
import datetime



def index(request):
	context = {
		'notes': Post.objects.all(),

	}
	return render(request, "django_notes_app/index.html", context)

def addnote(request):
	print 'add note'
	if request.method != 'POST':
		return redirect('/')
	else:
		print request.POST
		post = Post.objects.create(notes=request.POST['note'])

		# if len(request.POST.get('note'))<=0:
		# 	messages.error(request,'please enter something!')
		# 	print 'you didn'
		# 	return redirect('/')
		# else:
		# 	bound_form = PostForm(request.POST)	
		# 	if bound_form.is_valid():
		# 		Post.objects.create(notes=request.POST['note'])	
		# 	print note

			#if AJAX expects HTML in the response, then return an HTML string
		return HttpResponse("<div class='note'><h1>{}</h1></div>".format(post.notes))

			#return a json object if you are you submitting the form via AJAX


			# return redirect('addnote')
