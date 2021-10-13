import json
from django.http import HttpResponse
from orders.services.orderService import OrderServiceImple
from ResponseUtil import Response


def orders(request):
    if request.method == 'GET':
        order_list_json = OrderServiceImple().getAllOrders()
        response = Response().success(order_list_json)
        return HttpResponse(json.dumps(response), content_type="application/json")
    elif request.method == 'POST':
        requestDict = eval(request.body)
        if requestDict:
            result = OrderServiceImple().addOrder(requestDict)
            response = Response().success(result)
            return HttpResponse(json.dumps(response), content_type="application/json")
    response = Response().failed()
    return HttpResponse(json.dumps(response), content_type="application/json")


def certainOrder(request, order_id):
    if request.method == 'GET':
        order_json = OrderServiceImple().getOrderByOrderID(order_id)
        if order_json == None:
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
        response = Response().success(order_json)
        return HttpResponse(json.dumps(response), content_type="application/json")

    response = Response().failed()
    return HttpResponse(json.dumps(response), content_type="application/json")
