from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from instasafe.forms import UsernameForm
import requests
import json
import visionex_ig as vision

class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        form = UsernameForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = UsernameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #print post.test
            #print type(post)
            text = form.cleaned_data['post']
            form = UsernameForm()
            return redirect('https://api.instagram.com/oauth/authorize/?client_id=f2b7bbfe23954b10bb0f021ca294afc5&redirect_uri=http://localhost:8000/username&response_type=code')
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

class RedirectView(TemplateView):
    template_name = 'username.html'
    def get(self, request):
        userid = request.GET.get('user')
        code = request.GET.get('code')
        if(code):
            acc_token_url = "https://api.instagram.com/oauth/access_token"
            c_id = "f2b7bbfe23954b10bb0f021ca294afc5"
            client_secret = "3ccd0314fd4a41d0870bb13169dd1b6a"
            grant_type = "authorization_code"
            redirect_uri = "http://localhost:8000/username"
            args = {'code':code, "client_id" : c_id, "grant_type" : grant_type, "redirect_uri" : redirect_uri, "client_secret" : client_secret}
            r = requests.post(acc_token_url, data=args)
            print "[SENT ACC TOKEN POST] = " + str(r.status_code)
            dict_string = r.text
            json_acceptable_string = dict_string.replace("'", "\"")
            dict_ = json.loads(json_acceptable_string)
            print(dict_["access_token"])
            acc_token = dict_["access_token"]
            answer = vision.get_user_data(acc_token)
            print answer
        return render(request, self.template_name, answer)

    def post(self, request):
        print "[RECEIVED POST]"
