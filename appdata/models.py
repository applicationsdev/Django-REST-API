from django.db import models

# Models definitions
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=60)
    title = models.CharField(max_length=40)
    short_desc = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    instock_qty = models.IntegerField()
    net_price = models.DecimalField(max_digits=5, decimal_places=2)
    cat_id = models.IntegerField()
    subcat_id = models.IntegerField()
    vendor_id = models.IntegerField()
    
    def __str__(self):
        return self.title
