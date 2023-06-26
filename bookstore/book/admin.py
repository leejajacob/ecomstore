from django.contrib import admin
from .models import Book, Cart, CartItem, order

# Register your models here.
admin.site.register(Book)
admin.site.register(order)
admin.site.register(Cart)
admin.site.register(CartItem)

