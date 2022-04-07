from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login_check', views.login_check, name="login_check"),
    path('logout', views.logout, name="logout"),
    path('signup', views.signup, name="signup"),
    path('signup_check', views.signup_check, name="signup_check"),
]