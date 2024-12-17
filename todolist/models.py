from django.db import models
#from django.core.validators import MinLengthValidator

# Create your models here.


class Todo(models.Model):

    content = models.CharField(max_length=50)
    title = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.content