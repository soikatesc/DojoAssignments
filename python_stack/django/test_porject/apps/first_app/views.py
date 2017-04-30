from django.shortcuts import render,HttpResponse

#Controller
# Create your views here.


def index(request):
	print "*"*50
  	return render(request, 'index.html')
