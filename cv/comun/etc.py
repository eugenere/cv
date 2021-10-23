#
#
#


def pip_install(aPackage):
    import pip
    pip.main(['install', aPackage])


def get_date_time(format="%M-%S-%f"):
    import datetime
    assert isinstance(format, str), "Format isn't string"
    dateTimeStr = datetime.datetime.now().strftime(format)
    return dateTimeStr

    
def get_caller():
    from os.path import basename
    from inspect import getframeinfo, stack
    caller = getframeinfo(stack()[2][0])
    return fmt("%s:%03d"% (basename(caller.filename), caller.lineno))
    

def dbg(msg, *args, **kwargs):
    import logging
    from inspect import getframeinfo, stack
    caller = getframeinfo(stack()[1][0])
    logging.getLogger('dbg').debug("[%s] %s" % (
            get_caller(), msg.format(*args, **kwargs)))
        
        
def dump(data):
    import logging
    log = logging.getLogger('dump')
    log.debug(data)


def call_it_safe(aDef='False'):
    def decorator(aFunc):
        def wrapper():
            try:
                return aFunc()
            except:
                return aDef
        return wrapper
    return decorator


def python_ver():
    import sys
    ver = '{0}.{1}.{2}'.format(
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro)
    return ver


@call_it_safe('not found')
def django_ver():
    import django
    ver = django.get_version()
    return ver

    
@call_it_safe('not found')
def django_cms_ver():
    from cms import __version__ as ver
    return ver


def cmn_ver():
    from . import __version__ as ver
    return ver


def get_project_name():
    from os import environ
    
    return environ.get("PROJECT_NAME")
    
    
def dj_setup(project_name=get_project_name()):
    import django, os
        
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", project_name + ".settings")
    django.setup()


def get_session():
    from importlib import import_module
    from django.conf import settings
    return import_module(settings.SESSION_ENGINE).SessionStore()

    
def is_class(object):
    import types
    class ClassType:
        pass
    return type(object) == type(ClassType)


def is_func(object):
    import types
    return isinstance(object, (type, types.FunctionType))


def url_read(url):
    from urllib.request import urlopen
    data = urlopen(url).read();
    return data.decode('utf-8', 'ignore');


def f_read(file_name):
    text = None
    
    with open(file_name) as file:
        text = file.read()
    
    return text
    
    
def f_append(file_name, text):
    with open(file_name, 'a') as file:
        file.write(text)

        
def fb_append(file_name, bytes):
    with open(file_name, 'ab') as file:
        file.write(bytes)
        
        
def dj_call(name, *args, **kwargs):
    from django.core.management import call_command
    call_command(name, *args, **kwargs)

    
def fmt(str, *args, **kwargs):
    return str.format(*args, **kwargs)
        
        
def add_con_log(name):
    import logging
    logging.getLogger(name).addHandler(logging.StreamHandler())


def def_enc(str, codepage='ascii'): #cp1251, cp866
    if str:
        return str.encode('utf-8').decode('ascii', 'ignore')
    return ""


def get_files_num(path):
    import os
    path, dirs, files = next(os.walk(path))
    return len(files)


