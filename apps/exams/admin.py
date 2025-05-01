from django.contrib import admin
from .models import Settings, FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)

admin.site.register(Settings)