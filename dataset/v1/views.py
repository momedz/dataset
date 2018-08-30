# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from dataset.views import views
from dataset.dataset import update as fileDataset

# Create your views here.
fileDataset.configpath = "/dataset/dataset/dataset"
def datasets(request):
    return HttpResponse(fileDataset.information())

def dataset(request, *args, **kwargs):
    filename = kwargs.get('name')
    return HttpResponse(fileDataset.getFile(file=filename))

def dataset_normalize(request, *args, **kwargs):
    filename = kwargs.get('name')
    return HttpResponse(fileDataset.getFile(file=filename,normalize=True))