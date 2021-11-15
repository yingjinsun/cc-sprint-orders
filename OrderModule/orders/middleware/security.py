from ResponseUtil import Response
import json
from django.http import HttpResponse
from orders.services.orderService import OrderServiceImple
from ResponseUtil import Response
from ConstantUtil import Constant


class Security:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before request
        # Without login only can view product information
        dic = {'path': '/infos/products', 'method': 'POST'}
        auth = before_request(request, dic)
        if auth:
            response = self.get_response(request)
        else:
            response = Response().resp(Constant().NOT_LOGIN, None)
            response = HttpResponse(json.dumps(response), content_type="application/json")
        # After request

        return response


def before_request(request, dic):
    if request.path not in dic['path'] and request.method not in dic['method']:
        if not request.user.is_authenticated:
            return False
    return True
