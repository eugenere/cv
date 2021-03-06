from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
import json

import os
from django import conf

from quatropack import data
from . import data as new_data

from comun.etc import dbg


def common_context(request):
    return {
        'url_end': request.path.split('/')[-2],
        'machine_names': new_data.MACHINE_NAMES,
    }


def home(request):
    return render(request, 'quatropack2/index.html', dict({
        'logotypes': new_data.LOGOTYPES,
        'products': new_data.PRODUCTS,
        'peeling_shots': new_data.PEELING_SHOTS,
    }, **common_context(request)))


def home1(request):
    return render(request, 'quatropack2/index1.html', dict({
        'logotypes': new_data.LOGOTYPES,
        'products': new_data.PRODUCTS,
        'peeling_shots': new_data.PEELING_SHOTS,
    }, **common_context(request)))


def machines(request):
    return render(request, 'quatropack2/machines.html', dict({
        'machines': new_data.MACHINES,
    }, **common_context(request)))


def machine(request, slug):
    if slug not in new_data.MACHINES_BY_SLUG:
        return render(request, 'quatropack2/404.html', common_context(request))
    return render(request, 'quatropack2/{}.html'.format(slug[len("super_seal_"):]), dict({
            'machine': new_data.MACHINES_BY_SLUG[slug],
            'logotypes': new_data.LOGOTYPES,
            'products': new_data.PRODUCTS,
        }, **common_context(request)))
      
    """
    if "super_seal_max" == slug:
        return render(request, 'quatropack2/machine2.html', dict({
            'machine': new_data.MACHINES_BY_SLUG[slug],
            'logotypes': new_data.LOGOTYPES,
            'products': new_data.PRODUCTS,
        }, **common_context(request)))
    if "super_seal_100" == slug:
        return render(request, 'quatropack2/machine3.html', dict({
            'machine': new_data.MACHINES_BY_SLUG[slug],
            'logotypes': new_data.LOGOTYPES,
            'products': new_data.PRODUCTS,
        }, **common_context(request)))
    if "super_seal_50" == slug:
        return render(request, 'quatropack2/machine4.html', dict({
            'machine': new_data.MACHINES_BY_SLUG[slug],
            'logotypes': new_data.LOGOTYPES,
            'products': new_data.PRODUCTS,
        }, **common_context(request)))
    if "super_seal_75" == slug:
        return render(request, 'quatropack2/machine5.html', dict({
            'machine': new_data.MACHINES_BY_SLUG[slug],
            'logotypes': new_data.LOGOTYPES,
            'products': new_data.PRODUCTS,
        }, **common_context(request)))
    if slug in ["super_seal_100", "super_seal_75", "super_seal_50", "super_seal_touch", "super_seal_max"]:
        return render(request, 'quatropack2/{}.html'.format(slug[len("super_seal_"):]), dict({
            'machine': new_data.MACHINES_BY_SLUG[slug],
            'logotypes': new_data.LOGOTYPES,
            'products': new_data.PRODUCTS,
        }, **common_context(request)))
    

    return render(request, 'quatropack2/machine.html', dict({
        'machine': new_data.MACHINES_BY_SLUG[slug],
        'logotypes': new_data.LOGOTYPES,
        'products': new_data.PRODUCTS,
    }, **common_context(request)))
    """


def benefits(request):
    return render(request, 'quatropack2/benefits.html', dict({
        'benefits': new_data.BENEFITS,
    }, **common_context(request)))


def cases(request):
    """
    return render(request, 'quatropack2/cases.html', dict({
        'cases': data.REVIEWS,
    }, **common_context(request)))
    """
    return render(request, 'quatropack2/cases.html', common_context(request))


def media(request):
    return render(request, 'quatropack2/media.html', common_context(request))


def feedback(request, name):
    return render(request, 
            'quatropack2/{}.html'.format(name), 
            common_context(request))

    
def contacts(request):
    return render(request, 'quatropack2/contacts.html', dict({
        'data': {
            'image': '',
            'link': '',
            'title': '',
        }
    }, **common_context(request)))


def legal_terms(request):
    return render(request, 'quatropack2/terms.html', common_context(request))


def privacy_policy(request):
    return render(request, 'quatropack2/fake.html', common_context(request))


def technology(request):
    return render(request, 'quatropack2/technology.html', common_context(request))

def fake(request):
    return render(request, 'quatropack2/fake.html', common_context(request))
