from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'uploaded_at')

admin.site.register(Book, BookAdmin)