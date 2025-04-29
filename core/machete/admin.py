from django.contrib import admin
from .models import Contact, ClickWhatsApp

admin.site.site_header = "MACHETE Administrator"
admin.site.site_title = "MACHETE Administrator"
admin.site.index_title = "MACHETE Administrator"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'unsubscribed')
    search_fields = ('name', 'email')
    list_filter = ('unsubscribed', 'created_at')
    ordering = ('-created_at',)

@admin.register(ClickWhatsApp)
class ClickWhatsAppAdmin(admin.ModelAdmin):
    list_display = ('country', 'button', 'created_at')
    search_fields = ('country', 'button')
    list_filter = ('created_at',)
    ordering = ('-created_at',)