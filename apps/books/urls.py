from django.urls import path
from apps.books.views import book_list, book_detail, create_book, download_book

urlpatterns = [ 
    path('', book_list, name='books'), 
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('download/<int:pk>/', download_book, name='download-book'),
    path('add/', create_book, name='book-add'), 
]