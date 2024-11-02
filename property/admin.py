from django.contrib import admin
from .models import Flat, Complaint, Owner, PropertyOwnerOwnedFlats


class PropertyOwnerInline(admin.TabularInline):
    model = PropertyOwnerOwnedFlats
    extra = 1
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'has_balcony', 'rooms_number']
    raw_id_fields = ['liked_by']

    inlines = [PropertyOwnerInline]

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'text']
    raw_id_fields = ['flat']

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'owner_pure_phone')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
