from django.db import models
from apps.todo.models import User

# Create your models here.

class ToDolist(models.Model):
    title = models.CharField('Новое задания', max_length=555)
    is_complete = models.BooleanField( 'Завершено',default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        