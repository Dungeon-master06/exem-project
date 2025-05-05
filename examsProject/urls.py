from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('apps.books.urls')),
    path('exams/', include('apps.exams.urls')),
    path('auth/', include('apps.users.urls')), 
    path('', include('apps.settingis.urls')),  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)