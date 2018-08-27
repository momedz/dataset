# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dataset.views import views

# Create your views here.
def datasets(request):
    return views.TODO

def dataset(request, *args, **kwargs):
    return views.TODO

def dataset_normalize(request, *args, **kwargs):
    return views.TODO