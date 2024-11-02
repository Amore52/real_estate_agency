from django.contrib import admin

from .models import Flat, Complaint, Owner

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ['new_building', 'has_balcony', 'rooms_number']
    raw_id_fields = ['liked_by']

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'text']
    raw_id_fields = ['flat']

class OwnerAdmin (admin.ModelAdmin):
    list_display = ['user', 'owners_phonenumber', 'owner_pure_phone']
    raw_id_fields = ['flats']


admin.site.register(Flat, AuthorAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
