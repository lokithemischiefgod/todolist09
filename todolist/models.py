from django.db import models
#from django.core.validators import MinLengthValidator

# Create your models here.


class Todo(models.Model):

    content = models.TextField()
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.content