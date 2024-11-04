from django.contrib import admin
from .models import Flat, Complaint, Owner


class PropertyOwnerInline(admin.TabularInline):
    model = Owner.flats.through
    extra = 1
    raw_id_fields = ('owner',)

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'has_balcony', 'rooms_number']
    raw_id_fields = ['liked_by']
    inlines = [PropertyOwnerInline]

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'text']
    raw_id_fields = ['flat']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'pure_phone')


