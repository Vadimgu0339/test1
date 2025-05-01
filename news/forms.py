from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'date']

        widgets = {
            'title' : TextInput({
                'class' : 'form-control',
                'placeholder' : 'Название статьи', 
            }),
            'anons' : TextInput({
                'class' : 'form-control',
                'placeholder' : 'Анонс статьи', 
            }),
            'text' : Textarea({
                'class' : 'form-control',
                'placeholder' : 'Текст статьи', 
            }),
            'date' : DateTimeInput({
                'class' : 'form-control',
                'placeholder' : 'Дата публикации', 
            })
        }