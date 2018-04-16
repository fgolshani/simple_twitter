"""pug URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookstore import views
from django.conf.urls import url
from django.contrib.auth.views import logout

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.index, name="home"),
    url(r'signup/$', views.signup, name='signup'),
    url(r'logout/$', logout, {'next_page': "login"}, name="logout"),
    url(r'login/$', views.login, name="login"),
    url(r'add_tweet/$', views.add_tweet, name="add"),
    url(r'add_comment/$', views.add_comment, name="add_comment"),
    url(r'delete_tweet/$', views.delete_tweet, name="remove_comment"),
    url(r'edit_tweet/$', views.edit_tweet, name="edit_comment")
]
