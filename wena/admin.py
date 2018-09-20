from django.contrib import admin
from .models import Location, Photo


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['description', ]
    prepopulated_fields = {'slug': ('name', )}


