from django.contrib import admin
from .models import ShortLink


@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_code', 'original_url')
    list_display_links = ('user','short_code',)

