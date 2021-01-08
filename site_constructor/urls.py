from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from .views import *


urlpatterns = [
    path('', index, name='home_page'),
    url(r'^search/$', SearchView.as_view(), name="search"),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    url(r'^site_profile/$', SiteProfileView.as_view(), name='site_profile'),
    url(r'^sign_in/$', user_login, name='sign_in'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^mentors/$', mentors, name='mentors'),
]