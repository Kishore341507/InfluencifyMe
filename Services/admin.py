from django.contrib import admin
from .models import Service, Review

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Service)

admin.site.register(Review)



# Register your models here.
