from django.shortcuts import render, redirect
# from django.contrib import messages
from .models import *

# Create your views here.


def index(request):

	return render(request, "interest_app/home.html")

def add(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		# if len(request.POST.get('name')) == 0:
			#fast fail!!!!
		# user = User.objects.filter(name=request.POST.get('name'))
		# interest = Interest.objects.filter(interest=request.POST.get('interest'))
		# print User.objects.filter(name= request.POST['name']).first()
		if user == None:
			user = User.objects.create(name= request.POST['name'])
			if interest == None:
				interest = Interest.objects.create(interest= request.POST['interest'])
				user.interest.add(interest)

		if request.POST['name'] > 2 and interset == None:
			user = User.objects.get(name= request.POST['name'])
			interest = Interest.objects.create(interest= request.POST['interest'])
			user.interest.add(interest)

		if request.POST['name'] > 2 and interest != None:
			user = User.objects.get(name= request.POST['name'])
			interest = Interest.objects.get(interest= request.POST['interest'])
			user.interest.add(interest)


		return redirect('/users')

def users(request):
	context = {
		'users': User.objects.all()
	}		
	return render(request,"interest_app/users.html",context)

def show(request,userid):
	print userid
	context = {
		'user': User.objects.get(id=userid)
	}		
	
	return render(request,"interest_app/show.html",context)