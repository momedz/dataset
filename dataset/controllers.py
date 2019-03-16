import json
from django.http import JsonResponse, HttpResponse
from .services import information, json_file
from pymongo import MongoClient

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

# import random
# client = MongoClient('10.80.37.208', 27017)
# # client['dataset'].create_collection('test')
# db = client['dataset']
# test = db['test']
# name = "Karn"
# surname = "Klawmprasrerdh"
# test.insert_one({
#     "name": name,
#     "random": random.sample(range(777), 4)
# })
# print(db.collection_names(include_system_collections=True))
