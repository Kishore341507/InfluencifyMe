from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone') 


admin.site.register(Contact, ContactAdmin)

admin.site.site_header = 'Serials Chess Academy'
admin.site.site_title = 'SCA'
admin.site.index_title = 'Welcome to SCA Admin'
# admin.site.site_url = 'http://tickar.com'
