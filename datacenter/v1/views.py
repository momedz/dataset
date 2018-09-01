# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from datacenter.views import views
from datacenter.dataset import update as fileDataset

# Create your views here.
fileDataset.configpath = "/datasetcontroller/datacenter/dataset"
@csrf_exempt
def datasets(request):
    try:
        name = request.META["HTTP_X_ACCESS"]
        return HttpResponse(fileDataset.information())
    except:
        return views.ERROR400

@csrf_exempt
def dataset(request, *args, **kwargs):
    try:
        name = request.META["HTTP_X_ACCESS"]
        try:
            filename = kwargs.get('name')
            data = fileDataset.getFile(file=filename)
            return HttpResponse(data)
        except:
            return views.ERROR404
    except:
        return views.ERROR400

@csrf_exempt
def dataset_normalize(request, *args, **kwargs):
    try:
        name = request.META["HTTP_X_ACCESS"]
        try:
            filename = kwargs.get('name')
            data = fileDataset.getFile(file=filename,normalize=True)
            return HttpResponse(data)
        except:
            return views.ERROR404
    except:
        return views.ERROR400