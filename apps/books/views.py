from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import Book, Category
from apps.exams.models import Settings
from .form import BookForm, CategoryForm
from django.shortcuts import redirect

def book_list(request):
    settings = Settings.objects.all()
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        books = Book.objects.filter(category_id=category_id)
    else:
        books = Book.objects.all()
    context = {
        'books': books,
        'settings': settings,
        'categories': categories,
        "category_id": category_id
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

def create_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES)
        category_form = CategoryForm(request.POST)

        if 'add_category' in request.POST and category_form.is_valid():
            new_cat = category_form.save()
            return redirect(request.path + f'?category={new_cat.id}')

        if book_form.is_valid():
            book_form.save()
            return redirect('books')
    else:
        book_form = BookForm()
        category_form = CategoryForm()

    return render(request, 'pages/book_form.html', {
        'book_form': book_form,
        'category_form': category_form,
    })
