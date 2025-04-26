from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'pages/books.html', {'books': books})

def download_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return FileResponse(book.file.open('rb'), as_attachment=True, filename=book.file.name)
