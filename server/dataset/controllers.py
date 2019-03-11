import json
from django.http import JsonResponse, HttpResponse
# Create your views here.

class Out(object):
    def __init__(self, data):
        self.data = data
    def toDict(self):
        return self.__dict__
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
            
def index(request):
    data = Out("Test Object").toDict()
    return JsonResponse(data)