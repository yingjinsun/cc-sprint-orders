from datetime import datetime

from django.forms import model_to_dict
from orders.models import Order


class OrderServiceImple(object):

    def getAllOrders(self):
        lt = []
        for order in Order.objects.all().iterator():
            lt.append({
                "orderID": order.orderID,
                "userID": order.userID,
                "productID": order.productID,
                "quantity": order.quantity,
                "createDate": order.createDate.strftime("%Y-%m-%d %H:%M:%S"),
                "status": order.status
            })
        return lt

    def addOrder(self, request):
        newOrder = Order(userID=request.get('userID'),
                         productID=request.get('productID'),
                         quantity=request.get('quantity'),
                         createDate=request.get('create_date'),
                         status=request.get('status')
                         )
        newOrder.save()
        return "Success!"

    def updateOrder(self, request, order_id):
        order = Order.objects.get(orderID=order_id)
        order.userID = request.get('userID')
        order.productID = request.get('productID')
        order.quantity = request.get('quantity')
        order.createDate = request.get('create_date')
        order.status = request.get('status')
        order.save()
        return "Success!"

    def deleteOrder(self, order_id):
        Order.objects.get(orderID=order_id).delete()
        return "Success!"

    def getOrderByOrderID(self, order_id):
        order = Order.objects.filter(orderID=order_id)
        if len(order) == 0:
            return None
        order = list(order.values())[0]
        res = {
            "userID": order["userID"],
            "productID": order["productID"],
            "quantity": order["quantity"],
            "createDate": order["createDate"].strftime("%Y-%m-%d %H:%M:%S"),
            "status": order["status"]
        }
        return res

    def getOrderByPara(self, paras):
        query, fields, limit, offset = parseParas(paras)
        orders = Order.objects.filter(**query)
        fieldSet = fields.split(",")
        lt = []
        for order in orders.values():
            dict = {}
            for field in fieldSet:
                if field == 'create_date':
                    dict["createDate"] = order["createDate"].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    dict[field] = order[field]
            lt.append(dict)
        return lt[offset:offset+limit]

def parseParas(paras):
    fields = 'orderID,userID,productID,quantity,create_date,status'
    limit = 10
    offset = 0
    query = {}
    for key in paras:
        if key == 'orderID':
            query['orderID'] = int(paras.get(key))
        if key == 'userID':
            query['userID'] = int(paras.get(key))
        if key == 'productID':
            query['productID'] = int(paras.get(key))
        if key == 'quantity':
            query['quantity'] = int(paras.get(key))
        if key == 'create_date':
            query['createDate'] = paras.get(key)
        if key == 'status':
            query['status'] = datetime.strptime(paras.get(key), "%Y-%m-%d %H:%M:%S")
        if key == 'fields':
            fields = paras.get(key)
        if key == 'limit':
            limit = int(paras.get(key))
        if key == 'offset':
            offset = int(paras.get(key))
    return query, fields, limit, offset
