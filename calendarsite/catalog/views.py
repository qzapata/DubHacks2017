# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'index.html')

def task(request):
	return render(request, 'task.html')

def get_data(request):
	data = request.POST.getlist('data[]')
	print(tasks)
	return HttpResponse('success')
