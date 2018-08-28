# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from dataset.views import views
from dataset.dataset import update as fileDataset

# Create your views here.
def datasets(request):
    fileDataset.configpath = "/dataset/dataset/dataset"
    return HttpResponse(fileDataset.information())

def dataset(request, *args, **kwargs):
    return views.TODO

def dataset_normalize(request, *args, **kwargs):
    return views.TODO