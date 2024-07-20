from django.contrib import admin
from .models import Product
admin.site.register(Product)
from .models import CartItem
admin.site.register(CartItem)
from .models import Transaction
admin.site.register(Transaction)
from. models import LineItem
admin.site.register(LineItem)