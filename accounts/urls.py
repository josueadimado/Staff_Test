from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.login, name="login"),
    url(r'^accounts/forgot-password/$', views.forgot, name="forgot"),
    url(r'^accounts/register/$', views.register, name="register"),
    url(r'^accounts/index/$', views.index, name="index"),
    url(r'^accounts/test/$', views.test, name="test"),
]