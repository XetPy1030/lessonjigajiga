from django.http import HttpResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from pprint import pprint


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Create your views here.
def index(request: WSGIRequest):
    host = request.get_host()
    browser = request.META['HTTP_USER_AGENT']
    ip = get_client_ip(request)
    return HttpResponse('<br>'.join([host, browser, ip]))

def error(request: WSGIRequest):
    return HttpResponse('К сожалению произошла ошибка. Страница не найдена', status=404)

def user(req: WSGIRequest, name: str='Askar', folder: str='askar/', num_post: int='10'):
    return HttpResponse('<br>'.join([name, folder, num_post]))
