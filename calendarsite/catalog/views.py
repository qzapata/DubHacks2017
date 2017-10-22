# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

import Parser
import Event

# Create your views here.
def index(request):
	return render(request, 'index.html')

def task(request):
	return render(request, 'task.html')

def get_data(request):
    data = request.POST.getlist('tasks[]')
    p = Parser.parser(data)
    l= []
    for e in p.events:
        l.append(e.start.__str__())
        l.append(e.end.__str__())
        l.append(e.name)
    print(l)
    return HttpResponse('success')



