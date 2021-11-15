from django.db import models


# Create your models here.

class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    userID = models.IntegerField()
    productID = models.IntegerField()
    quantity = models.IntegerField(default=1)
    createDate = models.DateTimeField(max_length=50, auto_now=True)
    status = models.CharField(max_length=100)


class User(models.Model):

    userID = models.AutoField(primary_key=True)
    nameLast = models.CharField(max_length=50)
    nameFirst = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    userAddress = models.CharField(max_length=50)

    class Meta:
        db_table = 'infos_user'
