from django import forms


# Create your models here.

class LoginForm(forms.Form):
    # создаем поля формы, которые должны отображаться в форме на сайте
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


