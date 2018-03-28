from django.conf.urls import url
from instasafe import views

urlpatterns= [
    url(r'^$', views.HomePageView.as_view()),
    url(r'your-name/', views.HomePageView.as_view()),
    url(r'/thanks/^$', views.HomePageView.as_view()),

]
