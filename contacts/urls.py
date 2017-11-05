from django.conf.urls import url, include
from rest_framework import routers
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^new/$', views.new, name='new'),
    url(r'^react/$', views.react, name='react'),
    url(r'^api/contacts/$', views.ContactList.as_view(), name='api_contacts'),
]
