
from django.contrib import admin
from .models import Author, Publisher, Book, Customer, Order

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Order)

