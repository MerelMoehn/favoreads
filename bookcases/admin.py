from django.contrib import admin
from .models import Book, Bookcase, Bookcase_book
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'approved', 'created_on')
    search_fields = ['title', 'author']
    list_filter = ('approved', 'created_on')
    actions = ['approve_books']

    def approve_books(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Bookcase)
class BookcaseAdmin(SummernoteModelAdmin):

    list_display = ('owner', 'created_on')
    search_fields = ['owner']


@admin.register(Bookcase_book)
class Bookcase_bookAdmin(SummernoteModelAdmin):
    
    list_display = ('bookcase_id', 'book_id')
    search_fields = ['bookcase_id']
