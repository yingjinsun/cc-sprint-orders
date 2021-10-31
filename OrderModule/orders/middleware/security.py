from ResponseUtil import Response
import json
from django.http import HttpResponse


class Security:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        return response
        # response = Response().failed()
        # return HttpResponse(json.dumps(response), content_type="application/json")
