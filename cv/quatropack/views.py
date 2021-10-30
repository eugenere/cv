from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect

import os
from django import conf

from . import data
from . import forms


@login_required
def edit_contacts(request):
    from etc.utils import dbg
    import json

    dbg('start')

    if request.method == 'POST':
        #print(request.FILES)
        #print(request.POST)
        #print(image)

        form = forms.ContactsEditForm(request.POST, request.FILES)
        image = request.FILES['image']
        dbg('edit: {}/{}/{}', image.name, request.POST['title'], request.POST['link'])

        if form.is_valid():
            with open(os.path.join(conf.settings.MEDIA_ROOT, image.name), 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            with open(os.path.join(conf.settings.DATA_DIR, 'contacts.json'), 'w+') as file:
                json.dump({
                    'title': request.POST['title'],
                    'link': request.POST['link'],
                    'image': conf.settings.MEDIA_URL+image.name,
                }, file, sort_keys=True, indent=4)

            dbg('finish edit')
            return HttpResponseRedirect('/contacts/')
    else:
        form = forms.ContactsEditForm()

    dbg('finish show')
    return render(request, 'quatropack/edit.html', {'form': form})


def contacts(request):
    import json

    with open(os.path.join(conf.settings.DATA_DIR, 'contacts.json'), 'r') as file:
        context = {
            'data': json.load(file),
        }
        context.update(base_context(request))
        return render(request, 'quatropack/contacts.html', context)
    return Http404('data broken')


def set_lang(request, lang):
    from django.utils import translation

    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang
    return redirect(request.META['HTTP_REFERER'])
    

def base_context(request):
    print(request.path.split('/')[:-1])
    return {
        'devices': data.DEVICES,
        'url_end': request.path.split('/')[-1],
    }


def index(request):
    context = {
        'benefits': data.BENEFITS,
        'examples': data.EXAMPLES,
        'logotypes': data.LOGOTYPES,
    }
    context.update(base_context(request))
    return render(request, 'quatropack/index.html', context)

def benefits(request):
    context = {
        'benefits': data.BENEFITS,
    }
    context.update(base_context(request))
    return render(request, 'quatropack/benefits.html', context)
    
def clients(request):
    context = {
        'reviews': data.REVIEWS,
    }
    context.update(base_context(request))
    return render(request, 'quatropack/clients.html', context)
    
#def tech(request, name):
def devices(request):
    context = {
        'benefits': data.BENEFITS,
        'reviews': data.REVIEWS,
        'examples': data.EXAMPLES,
    }
    context.update(base_context(request))
    return render(request, 'quatropack/devices.html', context)

def device(request, name):
    context = {
        'examples': data.EXAMPLES,
        'benefits': data.BENEFITS,
        'logotypes': data.LOGOTYPES,
    }
    context.update(data.DEVICES_BY_SLUG[name])
    context.update(base_context(request))
    return render(request, 'quatropack/device.html', context)
