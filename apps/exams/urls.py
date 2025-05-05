from django.urls import path 
from apps.exams import views
 
 
urlpatterns = [ 
    path('', views.test_list, name="test_list"),
    path('test/<int:test_id>/', views.take_test, name="take_test")
]