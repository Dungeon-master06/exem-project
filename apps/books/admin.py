from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'uploaded_at')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug' :('title',)}

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)