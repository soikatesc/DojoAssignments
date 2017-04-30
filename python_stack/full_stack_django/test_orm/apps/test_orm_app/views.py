from django.shortcuts import render, redirect
from .models import Blog,Comment

# Create your views here.

def index(request):

	context = {
		"blogs": Blog.objects.all()
		#select * from Blog
	}
	return render(request, "test_orm_app/index.html",context)

def blogs(request):
	#using ORM
	Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
	#insert into blogs (title,,created_at,updated_at) value(title, blog)
	return redirect('/')

