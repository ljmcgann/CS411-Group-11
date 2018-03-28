# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect



# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
    def getUsername(request):
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
            form = UsernameForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
            # redirect to a new URL:
        print "form is : ", form
        return HttpResponseRedirect(form)
            #return HttpResponseRedirect('/thanks/')
            #print form

    # if a GET (or any other method) we'll create a blank form
        #else:
            #form = UsernameForm()
        return render(request, 'username.html', {'form': form})
