from django.contrib import admin

from .models import Flat, Claim

class FlatAdmin(admin.ModelAdmin):
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_filter = ['new_building', 'town']
    raw_id_fields = ['liked_by']

class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']

admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)