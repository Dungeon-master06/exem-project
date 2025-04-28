from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import Book
from apps.exams.models import Settings

def book_list(request):
    books = Book.objects.all()
    settings = Settings.objects.all()
    context = {
        'books': books,
        'settings': settings
    }
    return render(request, 'pages/books.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    settings = Settings.objects.all()
    context = {
        'book': book,
        'settings': settings
    }
    return render(request, 'pages/book-detail.html', context)

def download_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return FileResponse(book.file.open('rb'), as_attachment=True, filename=book.file.name)
