# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse


class views:
    TODO = HttpResponse("""
    {
        "code": 200,
        "status": "TODO"
    }
    """)
    ERROR400 = HttpResponse("""
    {
        "code": 400,
        "error": {
            "message": "Bad Request - Missing header"
        }
    }""")
    ERROR404 = HttpResponse("""
    {
        "code": 404,
        "error": {
            "massage": "Not Found"
        }
    }
    """)
    ERROR500 = HttpResponse("""
    {
        "code": 500,
        "error": {
            massage: "Can't connect to Database"
        }
    }
    """)
# Create your views here.
def not_found(request):
    return views.ERROR404