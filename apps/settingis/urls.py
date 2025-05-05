from django.urls import path 
from apps.settingis import views
 
 
urlpatterns = [ 
    path('', views.home, name='home'), 
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'), 
]