from django.urls import path 
from apps.todo.views import register, user_login
from django.contrib.auth.views import LogoutView
urlpatterns = [  
    path('', register, name='register'),    
    path('login/', user_login, name='login'), 
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'), 
    
]