from django import template
from django.utils import safestring
from comun.etc import fmt, dbg as cdbg


register = template.Library()


@register.simple_tag
def define(str):
    return str


@register.simple_tag
def dbg(mensaje):
    from django.utils.html import format_html as fmt
    cdbg(fmt("dbg.tag: {}", mensaje))
    html = "<span class='dbg'>{}</span>"
    return fmt(html, mensaje)

