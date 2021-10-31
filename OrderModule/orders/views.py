import json
from django.http import HttpResponse
from orders.services.orderService import OrderServiceImple
from ResponseUtil import Response
from ConstantUtil import Constant


def orders(request):
    if request.method == 'GET':
        order_list_json = OrderServiceImple().getAllOrders()
        if not order_list_json:
            response = Response().failed()
        else:
            response = Response().success(order_list_json)
        return HttpResponse(json.dumps(response), content_type="application/json")
    elif request.method == 'POST':
        requestDict = eval(request.body)
        if requestDict:
            result = OrderServiceImple().addOrder(requestDict)
            response = Response().resp(Constant().POST, result)
            return HttpResponse(json.dumps(response), content_type="application/json")
    response = Response().failed()
    return HttpResponse(json.dumps(response), content_type="application/json")


def certainOrder(request, order_id):
    if request.method == 'GET':
        order_json = OrderServiceImple().getOrderByOrderID(order_id)
        if order_json is None:
            response = Response().failed()
        else:
            response = Response().success(order_json)
        return HttpResponse(json.dumps(response), content_type="application/json")

    elif request.method == 'PUT':
        requestDict = eval(request.body)
        if requestDict:
            result = OrderServiceImple().updateOrder(requestDict, order_id)
            response = Response().success(result)
            return HttpResponse(json.dumps(response), content_type="application/json")

    elif request.method == 'DELETE':
        order_json = OrderServiceImple().deleteOrder(order_id)
        response = Response().resp(Constant().DELETE, order_json)
        return HttpResponse(json.dumps(response), content_type="application/json")

    response = Response().failed()
    return HttpResponse(json.dumps(response), content_type="application/json")


def ordersWithField(request):
    paras = getParaFromURL(request)
    if not paras:
        return orders(request)
    response = OrderServiceImple().getOrderByPara(paras)
    if not response:
        response = Response().failed()
    return HttpResponse(json.dumps(response), content_type="application/json")


def getParaFromURL(request):
    dic = {}
    for key in request.GET:
        dic[key] = request.GET[key]
    return dic
