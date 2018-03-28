from rest_framework import serializers
from . models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            'sku',
            'title',
            'short_desc',
            'date_added',
            'instock_qty',
            'net_price',
            'cat_id',
            'subcat_id',
            'vendor_id',
        ]
