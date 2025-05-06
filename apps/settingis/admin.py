from django.contrib import admin
from .models import Settings, FAQ, SocialLink

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'icon',)

admin.site.register(Settings)