from django.contrib import admin
from .models import Plant, RatingPlant,Cart,Order
from firstone.models import PlantSize



class ReviewsInline(admin.StackedInline):
    model = RatingPlant
    extra = 1
    
class SizeInline(admin.TabularInline):
    model = PlantSize
    extra = 1
    

    
class PlantAdmin(admin.ModelAdmin):
    search_fields=['name']
    inlines = [SizeInline,ReviewsInline]
    
class CartAdmin(admin.ModelAdmin):
    search_fields = ['plantid']

class OrderAdmin(admin.ModelAdmin):
    search_fields = ['username']


admin.site.register(Plant,PlantAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Order,OrderAdmin)

# Register your models here.
