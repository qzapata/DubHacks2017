from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^/task$', views.task, name='task'),
	url(r'^get_data', views.get_data),
]