from django.contrib import admin
from .models import *

admin.site.site_header='FoodZone|Admin'
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','added_on','is_approved']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name','desinignation','image','added_on','update_on']
admin.site.register(Conatct,ContactAdmin)


admin.site.register(Team,TeamAdmin)
admin.site.register(Dish)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Forget)
