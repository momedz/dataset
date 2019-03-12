from django.urls import path

from . import controllers

urlpatterns = [
    path('', controllers.index, name='index'),
    path('<str:dataset>/', controllers.raw_data, name='raw_data'),
    path('<str:dataset>/normalize', controllers.normalize_data, name='normalize_data')
]