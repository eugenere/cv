from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'curriculum'

urlpatterns = [
    path('', TemplateView.as_view(template_name="curriculum/index.html"), name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('cv_pdf/', views.cv_pdf, name='cv_pdf'),
]
