from django.conf.urls import url
from instasafe import views
from django.views.generic import TemplateView

urlpatterns= [
    url(r'^$', views.HomeView.as_view()),
    url(r'home/', views.HomeView.as_view()),
    url(r'username/', views.RedirectView.as_view())

]
