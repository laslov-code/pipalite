from django.db import models

# Create your models here.
class Warehouse(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    class Meta:
        permissions = [
            ("can_assign_warehouse", "Can Assign Warehouse"),
        ]  

"""
class Inventory(models.Model):
    name = models.CharField(max_length=540)
    sku = models.CharField(max_length=50)
    barcode = models.CharField(max_length=50)
    price1 = models.BigIntegerField()
    price2 = models.BigIntegerField()
    price3 = models.BigIntegerField()
    cost = models.BigIntegerField()
    description = models.CharField(max_length=1000)
    product_image = models.ImageField(upload_to='inventory',default='defaults/inventory.png')

class Stocks(models.Model):
    warehouse=models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    inventory=models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity=models.BigIntegerField()

class Sets(models.Model):
    name = models.CharField(max_length=540)
    sku = models.CharField(max_length=50)
    barcode = models.CharField(max_length=50)
    price1 = models.BigIntegerField()
    price2 = models.BigIntegerField()
    price3 = models.BigIntegerField()
    description = models.CharField(max_length=1000)
    product_image = models.ImageField(upload_to='inventory',default='defaults/inventory.png')

class Subitem(models.Model):
    set = models.ForeignKey(Sets, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    factor = models.IntegerField()

    
"""