# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from instasafe.forms import UsernameForm



class HomeView(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        form = UsernameForm()
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = UsernameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = UsernameForm()
            return redirect('home/')
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
