from django.contrib import admin

from .models import FAQ, Category, Type, SubCategory

# Register your models here.

admin.site.register(FAQ)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(SubCategory)
