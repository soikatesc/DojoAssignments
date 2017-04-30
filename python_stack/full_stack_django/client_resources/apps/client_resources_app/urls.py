from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^client/add$',views.client_add),
	url(r'^client_add_post$',views.client_add_post),
	url(r'^client/(?P<clientid>\d+)$',views.client_profile),
	url(r'^(?P<clientid>\d+)/addproject$',views.addproject),
	url(r'^addprojectpost/(?P<clientid>\d+)$',views.addprojectpost),
	url(r'^show/projects/(?P<projectid>\d+)$',views.show_project),

]
