from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^add$',views.add),
	url(r'^users$',views.users),
	url(r'^show/(?P<userid>\d+)$',views.show),

]
