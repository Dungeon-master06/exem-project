from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import Book, Category
from apps.settingis.models import Settings, SocialLink
from .form import BookForm, CategoryForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator


def book_list(request): 
    settings = Settings.objects.order_by('-id').first()
    categories = Category.objects.all()
    social_links = SocialLink.objects.all()
    category_id = request.GET.get('category', '')
    search_query = request.GET.get('q', '')
    author_filter = request.GET.get('author', '')
    if category_id:
        books = Book.objects.filter(category__id=category_id)
    else:
        books = Book.objects.all()
    if search_query:
        books = books.filter(title__icontains=search_query)
    if author_filter:
        books = books.filter(author__icontains=author_filter)
    if 'filter' in request.GET:
        search_query = ''
        author_filter = ''
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'books': books,
        'settings': settings,
        'categories': categories,
        "category_id": category_id,
        'books': page_obj,
        'page_obj': page_obj,
        'selected_category': request.GET.get('category'),
        'search_query': search_query,
        'author_filter': author_filter,
        'social_links': social_links,
        'total_books': Book.objects.count(),
        'total_categories': Category.objects.count(),
    }
    return render(request, 'pages/books/books.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    settings = Settings.objects.order_by('-id').first()
    social_links = SocialLink.objects.all()
    context = {
        'book': book,
        'social_links': social_links,
        'settings': settings
    }
    return render(request, 'pages/books/book-detail.html', context)

def download_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return FileResponse(book.file.open('rb'), as_attachment=True, filename=book.file.name)

@staff_member_required(login_url='/login/')
def create_book(request):
    social_links = SocialLink.objects.all()
    settings = Settings.objects.order_by('-id').first()
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
    context = {
        'book_form': book_form,
        'category_form': category_form,
        'social_links': social_links,
        'settings': settings
    }
    return render(request, 'pages/books/book_form.html', context)
