from django.urls import path
from django.views.generic import TemplateView

#from . import views

app_name = 'ahorra_energia'

urlpatterns = [
    path('', TemplateView.as_view(template_name="ahorra_energia/inicio7.html"), name='inicio'),
    path('i', TemplateView.as_view(template_name="ahorra_energia/inicio.html"), name='inicio-cero'),
    path('1', TemplateView.as_view(template_name="ahorra_energia/inicio1.html"), name='uno'),
    path('2', TemplateView.as_view(template_name="ahorra_energia/inicio2.html"), name='dos'),
    path('3', TemplateView.as_view(template_name="/inicio3.html"), name='tres'),
    path('4', TemplateView.as_view(template_name="/inicio4.html"), name='quatro'),
    path('5', TemplateView.as_view(template_name="/inicio5.html"), name='cinco'),
    #path('6', TemplateView.as_view(template_name="nueva_vista/inicio6.html"), name='seis'),
    path('todos', TemplateView.as_view(template_name="ahorra_energia/all.html"), name='todos'),
    path('f', TemplateView.as_view(template_name="ahorra_energia/factura.html"), name='factura'),
    #path('nv', views.nuevo, name='nuevo'),
    #path('6', views.inicio, name='seis'),
    #path('6-1', views.inicio1, name='seis-1'),
    #path('6-2', views.inicio2, name='seis-2'),
    #path('6-3', views.inicio3, name='seis-3'),
    path('7', TemplateView.as_view(template_name="ahorra_energia/inicio7.html"), name='siete'),
]


"""
    url(r'^json/$', views.index_json, name='json'),
"""

