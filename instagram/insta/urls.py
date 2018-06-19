from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth.views import login,logout,logout_then_login,password_change,password_change_done
urlpatterns = [
    #url(r'^login/$', views.user_login, name='Login'),
    url(r'^login/$',login,name='login'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^logout_then_login/$',logout_then_login,name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^password-change/$',password_change,name='password_change'),
    url(r'^password-change/done/$',password_change_done,name='password_change_done'),
]

#if settings.DEBUG:
    #urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
