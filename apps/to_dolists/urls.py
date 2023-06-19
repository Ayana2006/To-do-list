from django.urls import path 
from apps.to_dolists.views import index, update
urlpatterns = [
    path('user/', index, name='index'),  
    path('update/<int:id>/', update, name='update'),    
    
]
