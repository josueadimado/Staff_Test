from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.tologin, name="login"),
    url(r'^accounts/login/$', views.mylogin, name="login-view"),
    url(r'^accounts/forgot-password/$', views.forgot, name="forgot"),
    url(r'^accounts/register/$', views.register, name="register"),
    url(r'^accounts/index/$', views.index, name="index"),
    url(r'^accounts/test/(?P<number>[-\w]+)/$', views.test, name="test"),
]