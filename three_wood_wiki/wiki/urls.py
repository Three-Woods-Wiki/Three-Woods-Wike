"""three_wood_wiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url
from wiki import views
from django.contrib import admin
import wiki

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login_page, name='login'),
    url(r'^register$', views.register_page, name='register'),
    url(r'^register_user$', views.register_user),
    url(r'^check_login$', views.check_login),
    url(r'^check_username$', views.check_username),
    url(r'^logout$', views.logout_page),
    url(r'^index/$', views.index, name='index'),
]
