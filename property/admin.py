from django.contrib import admin

from .models import Flat, Claim, Owner


class FlatAdmin(admin.ModelAdmin):
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by']


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']

class Owned_flatInline(admin.TabularInline):
    raw_id_fields = ['owner', 'flat']
    model = Flat.owned_flats.through


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['owned_flat']
    # list_display = ('display_flats',)
    search_fields = ['owner']
    inlines = [Owned_flatInline]

    # def display_flats(self):
    #     return ', '.join([flat.owner for flat in self.owned_flats.all()])
    #
    # display_flats.short_description = 'Flats'


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)