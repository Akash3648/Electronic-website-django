from django.contrib import admin
from servicemodel.models import service

class serviceAdmin(admin.ModelAdmin):
    list_display = ('service_icon','service_title','service_des')

admin.site.register(service, serviceAdmin)


