from django.urls import path
from django.views.generic.base import TemplateView

from . import views


app_name = 'quatropack'
urlpatterns = [
    path('', views.index, name='home'),
    path('setlang/<lang>', views.set_lang, name='setlang'),
    path('products', views.devices, name='devices'),
    path('product/<name>', views.device, name='device'),
    path('benefits/', views.benefits, name='benefits'),
    path('clients/', views.clients, name='clients'),
    path('editor/', views.edit_contacts, name='editor'),
    path('media/', TemplateView.as_view(template_name='quatropack/media.html'), name='media'),
    #path('contacts/', TemplateView.as_view(template_name='quatropack/contacts.html'), name='contacts'),
    path('contacts/', views.contacts, name='contacts'),
    path('privacy/', TemplateView.as_view(template_name='quatropack/privacy-policy.html'), name='privacy'),
    path('legally/', TemplateView.as_view(template_name='quatropack/legal-terms.html'), name='legally'),
    path('i/', TemplateView.as_view(template_name='quatropack/i.html'), name='i_html'),
]
