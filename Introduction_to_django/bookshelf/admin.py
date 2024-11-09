from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in list view
    search_fields = ('title', 'author')  # Fields to search
    list_filter = ('publication_year',)  # Filter options
    ordering = ('publication_year',)   # Order options

# Register your models here.
admin.site.register(Book, BookAdmin)