from django.db import models


# Create your models here.

class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    userID = models.IntegerField()
    productID = models.IntegerField()
    quantity = models.IntegerField(default=1)
    createDate = models.DateTimeField(max_length=50, auto_now=True)
    status = models.CharField(max_length=100)

