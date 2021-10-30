from django import forms
from django.utils.translation import gettext_lazy as _


class ContactsEditForm(forms.Form):
    title = forms.CharField(required=False, label=_('title'), max_length=255, localize=True, label_suffix='')
    link = forms.CharField(required=True, label=_('link'), max_length=255, localize=True, label_suffix='')
    image = forms.ImageField(label=_('image'), localize=True, label_suffix='')
