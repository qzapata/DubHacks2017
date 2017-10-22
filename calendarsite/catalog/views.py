# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import reverse


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
    l = []
    for e in p.events:
        l.append(e.start.__str__())
        l.append(e.end.__str__())
        l.append(e.name)
    print(l)
    #return HttpResponseRedirect(reverse("task"))
    return render_to_response('task.html', {'papel' : "l"}, RequestContext(request))


