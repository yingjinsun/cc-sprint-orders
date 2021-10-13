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
        print(lt)
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