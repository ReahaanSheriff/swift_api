from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CreateShipment(models.Model):
    orderId = models.CharField(max_length=25, primary_key=True)
    user_id_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField( auto_now_add=True)
    pname = models.CharField(max_length=50)
    pmobile = models.IntegerField()
    paddress = models.CharField(max_length=100)
    ppincode = models.IntegerField()
    pcity = models.CharField(max_length=50)
    pstate = models.CharField(max_length=50)
    pcountry = models.CharField(max_length=50)
    dname = models.CharField(max_length=50)
    dmobile = models.IntegerField()
    daddress = models.CharField(max_length=100)
    dcity = models.CharField(max_length=50)
    dstate = models.CharField(max_length=50)
    dpincode = models.IntegerField()
    dcountry = models.CharField(max_length=50)
    productName = models.CharField(max_length=50)
    productValue = models.IntegerField()
    weight = models.FloatField()
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    shippingPrice = models.IntegerField()
    estimateDate =  models.CharField(max_length=50)

class Tracking(models.Model):
    shipment = models.ForeignKey(CreateShipment, on_delete=models.CASCADE)
    pickScheduled = models.BooleanField(default = True)
    outForPickup = models.BooleanField()
    pickedUp = models.BooleanField()
    transit = models.BooleanField()
    outForDelivery = models.BooleanField()
    delivered = models.BooleanField()