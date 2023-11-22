from django.contrib import admin
from admin_panel.models import (
    PlasticWindowsCategories,
    PlasticWindowsGetCategories,
    Plastics,
    Windows,
    WindowsImages,
    Contacts,
    OurServices,
    OurServiceGet,
    OurWork,
)


@admin.register(PlasticWindowsCategories)
class PlasticWindowsCategoriesAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(PlasticWindowsGetCategories)
class PlasticWindowsGetCategoriesAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name"]

@admin.register(Windows)
class WindowsAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

@admin.register(WindowsImages)
class WindowsImagesAdmin(admin.ModelAdmin):
    list_display = ["id", "windows"]

@admin.register(OurWork)
class OurWorkAdmin(admin.ModelAdmin):
    list_display = ["id", "country"]

@admin.register(OurServices)
class OurServicesAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(OurServiceGet)
class OurServiceGetAdmin(admin.ModelAdmin):
    list_display = ["id", "ourservices"]

@admin.register(Plastics)
class PlasticsAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]