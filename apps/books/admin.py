from django.contrib import admin
from .models import Book, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug' :('title',)}

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'uploaded_at')
    filter_horizontal = ('category',)

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)