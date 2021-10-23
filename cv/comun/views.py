from django.http import Http404
from django.shortcuts import render

from .etc import dbg, fmt

# Create your views here.


def error_404(request, direccion):
    raise Http404("{} does not exist".format(direccion))

