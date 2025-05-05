from django.contrib import admin
from django.urls import path, include
from apps.books.views import (book_list, book_detail, create_book, download_book)
from apps.settingis import views
from apps.users.views import (login_view, reg_view, logout_view)

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('exams/', include('apps.exams.urls')),
    path('', views.home, name='home'),
    path('books/', book_list, name='books'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('download/<int:pk>/', download_book, name='download-book'),
    path('add/', create_book, name='book-add'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', reg_view, name='register'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)