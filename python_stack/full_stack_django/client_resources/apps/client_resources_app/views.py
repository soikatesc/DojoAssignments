from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
from django.db.models import Count


def index(request):
	context = {
		"clients" : Client.objects.all()
	}
	return render(request, "client_resources_app/index.html",context)

def client_add(request):
	return render(request, "client_resources_app/add_clients.html")

def client_add_post(request):
	if request.method != 'POST':
		return redirect('/client/add')

	else:
		business_name = request.POST['business_name']
		email = request.POST['email']
		phone = request.POST['phone']
		notes = request.POST['notes']

		Client.objects.create(
			business_name = business_name,
			email = email,
			phone = phone,
			notes = notes
			)

		return redirect('/')

def client_profile(request,clientid):
	print clientid
	context = {
		"client" : Client.objects.get(id = clientid),
		# "projects": Project.objects.all()
	}

	return render(request, "client_resources_app/client_profile.html",context)

def addproject(request,clientid):
	print clientid
	context = {
		"cliend_id" : clientid
	}
	return render(request, "client_resources_app/add_project.html",context)

def addprojectpost(request,clientid):
	print 'addprojectpost'
	project_name = request.POST['project_name']
	notes = request.POST['notes']
	project = Project.objects.create(
		project_name = project_name,
		notes = notes,
		client = Client.objects.get(id = clientid)
		)
	print 'project_id',project.id
	return redirect('/show/projects/{}'.format(project.id))

def show_project(request,projectid):
	context = {
		"project" : Project.objects.get(id=projectid)
	}

	return render(request, "client_resources_app/project_profile.html",context)

