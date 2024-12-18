from django.db import models
#from django.core.validators import MinLengthValidator

# Create your models here.


class Todo(models.Model):

    content = models.TextField()
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content