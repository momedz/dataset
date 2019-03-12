import json
from django.http import JsonResponse, HttpResponse
from .services import information, json_file

# Create your views here.

def index(request):
    def GET():
        return information()

    return HttpResponse({
                            'GET': GET
                        }[request.method]())


def raw_data(request, dataset):
    def GET():
        return json_file(dataset, normalize=False)

    return HttpResponse({
                            'GET': GET
                        }[request.method]())


def normalize_data(request, dataset):
    def GET():
        return json_file(dataset, normalize=True)

    return HttpResponse({
                            'GET': GET
                        }[request.method]())
