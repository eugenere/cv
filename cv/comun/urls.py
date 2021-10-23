from django.urls import path

from . import views

app_name = 'comun'

urlpatterns = [
    path('', views.error_404, name='404'),
    #path('new_form', views.new_form, name='new_form'),
    #path('buscar', views.buscar, name='buscar'),
]
