from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_list, name='test_list'),  # Теперь имя 'test_list' вместо 'exams'
    path('test/<int:test_id>/', views.take_test, name='take_test'),
]