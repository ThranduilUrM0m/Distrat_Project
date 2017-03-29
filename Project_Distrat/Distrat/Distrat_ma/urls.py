from django.conf.urls import *
from . import views
from django.shortcuts import render

app_name = 'Distrat_ma'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^about_us/$', views.about_us, name='about_us'),
    url('^engagements/$', views.engagements, name='engagements'),
    url('^$', views.products, name='products'),
    url('^samples/$', views.samples, name='samples'),
    url('^showrooms/$', views.showrooms, name='showrooms'),
    url('^(?P<categorie_id>[0-9]+)/categorie/$', views.categories, name='categories'),
    url('^(?P<souscategorie_id>[0-9]+)/subcategories/$', views.subcategories, name='subcategories'),
    url(r'^avis_register$', views.avis_register, name='avis_register'),
]