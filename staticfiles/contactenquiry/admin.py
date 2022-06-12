import imp
from django.contrib import admin
from contactenquiry.models import contactenquiry

class saveAdmin(admin.ModelAdmin):
    list_display=('contact_name','contact_email','contact_phone','contact_messege')

admin.site.register(contactenquiry, saveAdmin)


# Register your models here.
