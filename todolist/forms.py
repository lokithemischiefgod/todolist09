from .models import Todo
from django.forms import ModelForm, TextInput


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

        labels = {

            'title': 'Judul',
            'content': 'Deskripsi'
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'id': 'titleHere', 'aria-describedby': 'titleHelp', 'placeholder': 'Masukkan Judul'}),
            'content': TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp', 'placeholder': 'Masukkan Deskripsi'})
        }
        