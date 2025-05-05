from django.urls import path
from apps.users.views import login_view, reg_view, logout_view


urlpatterns = [ 
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', reg_view, name='register'),
]