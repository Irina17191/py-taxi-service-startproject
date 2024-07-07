from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from taxi.models import Manufacturer, Driver, Car


User = get_user_model()
# @admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number",)}),)


# @admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model", ]
    list_filter = ["manufacturer", ]


admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Driver, DriverAdmin)
