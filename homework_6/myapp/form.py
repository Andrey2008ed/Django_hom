from django import forms
from .models import Author, Posts


class GameForm(forms.Form):
    game = forms.ChoiceField(choices=[('М', 'Монета'), ('К', 'Кость'), ('Ч', 'Случайное Число')])
    number = forms.IntegerField(min_value=1, max_value=64)


# class AuthorForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     surname = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     biography = forms.CharField()
#     birthday = forms.DateField()

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'email', 'biography', 'birthday']


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['name_title', 'description', 'author', 'category', 'count_watching']

