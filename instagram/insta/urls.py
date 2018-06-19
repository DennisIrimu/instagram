from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    #url(r'^login/$', views.user_login, name='Login'),
    url(r'^login/$','django.contrib.auth.views.login',name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout',name='logout'),
    url(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login',name='logout_then_login')
]

#if settings.DEBUG:
    #urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
