from django.conf.urls import url
from . import views

urlspatterns = [
    url(r'^login/$', views.user_login, name='Login'),
]
