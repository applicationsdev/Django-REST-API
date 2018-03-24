from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    vendor = models.CharField(max_length=30)
    added = models.DateTimeField(auto_now_add=True)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.sku
