from django.shortcuts import render
from django.http import FileResponse
import os

# Create your views here.


def inicio(request):
    return render(request, 'curriculum/inicio.html')

def cv_pdf(request):
    filepath = os.path.join('static', 'curriculum', 'CvEugenioRepin.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
