from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
import datetime
# Create your views here.

def current_user(request):
	return User.objects.get(id=request.session['user_id'])



def index(request):

	return render(request, "belt_review_app/index.html")

def quotes(request):


	context = {
		'current_user' : current_user(request),
		'quotes': Quote.objects.all().exclude(favorites=current_user(request)),

	}

	return render(request, "belt_review_app/success.html",context)

def createquote(request):
	if request.method != 'POST':
		return redirect('/quotes')
	else:
		print 'createquotes'
		quote = Quote.objects.create(
			name = request.POST.get('name'),
			message = request.POST.get('message'),
			user = current_user(request),

			)
		return redirect('/quotes')

def favoritequote(request,quoteid):

	quote = Quote.objects.get(id=quoteid)
	print quote
	# print quote
	# print current_user(request)
	user = quote.favorites.add(current_user(request))
	return redirect('/quotes')

def removefavorite(request,quoteid):
	quote = Quote.objects.get(id=quoteid)
	user = quote.favorites.remove(current_user(request))
	return redirect('/quotes')

def userprofile(request,userid):

	context = {
	'user' : User.objects.get(id=userid),
	# 'quotes': Quote.objects.all().exclude(favorites=current_user(request)),

	}

	return render(request,"belt_review_app/users.html",context)






def createUser(request):
	if request.method != 'POST':
		return redirect('/')
	else:

		check = User.objects.validateUser(request.POST)
		if check[0] == False:
			for error in check[1]:
				print error
				messages.error(request,error)
			return redirect('/')

		else:
			dob=str(request.POST.get('dateofbirth'))
			dob_coverted=datetime.datetime.strptime(dob, '%Y-%m-%d').date()
			hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
			user = User.objects.create(
				name = request.POST.get('name'),
				alias = request.POST.get('name'),
				email = request.POST.get('email'),
				password = hashed_pw,
				dateofbirth = dob_coverted

			)
			print 'user_id: ',user.id
			request.session['user_id'] = user.id
			request.session['user_name'] = user.name
		return redirect('/quotes')



def login(request):
	print 'login'
	if request.method != 'POST':
		return redirect('/')
	else:
		#see if the email is in the db
		#
		user = User.objects.filter(email= request.POST.get('email')).first()
		if user and bcrypt.checkpw(request.POST.get('password').encode(),user.password.encode()):
			request.session['user_name'] = user.name
			request.session['user_id'] = user.id
			return redirect('/quotes')
		else:
			messages.error(request,'invalid')
			return redirect('/')

def logout(request):
	request.session.pop('user_name',None)
	return redirect('/')



