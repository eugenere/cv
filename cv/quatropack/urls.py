from django.urls import path,re_path
from django.views.generic.base import TemplateView

from . import views


app_name = 'quatropack'

urlpatterns = [
    #TODO: remove for continue
    #re_path(r'^.*$', TemplateView.as_view(template_name='quatropack2/tarde.html')),
    
    #re_path(r'^.*$', RedirectView.as_view(url='http://quatropack.com', permanent=True)),
    #path('media/', TemplateView.as_view(template_name='quatropack/media.html'), name='media'),
    #path('', views.fake, name='home'),
    #path('fake/', views.fake, name='fake'),
    
    #TODO: for work
    path('', views.home, name='home'),
    path('h1/', views.home1, name='home1'),
    
    path('machines/', views.machines, name='machines'),

    path('benefits/', views.benefits, name='benefits'),
    path('technology/', views.technology, name='technology'),
    path('cases/', views.cases, name='cases'),
    path('media/', views.media, name='media'),
    path('contacts/', views.contacts, name='contacts'),
    
    path('legal-terms/', views.legal_terms, name='legal-terms'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    
    path('probelte/', views.feedback, { "name": "probelte" }, name='probelte'),
    path('maripaz/', views.feedback, { "name": "maripaz" }, name='maripaz'),
    path('bestprotein/', views.feedback, { "name": "bestprotein" }, name='bestprotein'),
    path('esteve/', views.fake, name='esteve'),
    path('labrubio/', views.fake, name='labrubio'),
    
    path('top-pressure-seal/', views.fake, name='top-pressure-seal'),
    path('<str:slug>/', views.machine, name='machine'),
]

    
"""
    path('probelte/', TemplateView.as_view(template_name='quatropack2/probelte.html'), name='probelte'),
    path('maripaz/', TemplateView.as_view(template_name='quatropack2/maripaz.html'), name='maripaz'),
    path('bestprotein/', TemplateView.as_view(template_name='quatropack2/bestprotein.html'), name='bestprotein'),
"""
