from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^createUser$',views.createUser),
	url(r'^login$',views.login),
	url(r'^logout$',views.logout),
	url(r'^quotes$',views.quotes),
	url(r'^createquote$',views.createquote),
	url(r'^favoritequote/(?P<quoteid>\d+)$',views.favoritequote),
	url(r'^removefavorite/(?P<quoteid>\d+)$',views.removefavorite),
	url(r'^users/(?P<userid>\d+)$',views.userprofile),

]
