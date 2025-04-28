from django.contrib import admin
from django.urls import path
from apps.exams.views import (home, contact, faq)
from apps.books.views import (book_list, download_book, book_detail)

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('download/<int:pk>/', download_book, name='download-book'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)