from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from groupsapp.models import MyGroups


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class AddGroupForm(forms.Form):
    name = forms.CharField(max_length=50, label='Name of Group', widget=forms.TextInput(attrs={'class': 'form-input'}))
    countOfMembers = forms.IntegerField(label='Members now', widget=forms.TextInput(attrs={'class': 'form-input'}))
    MaxCountOfMembers = forms.IntegerField(label='Max members', widget=forms.TextInput(attrs={'class': 'form-input'}))
    is_open = forms.BooleanField(label='Is open')
    meeting_Date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    meeting_place = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    photo = forms.ImageField()
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = MyGroups
        fields = ['name', 'countOfMembers', 'MaxCountOfMembers', 'is_open', 'meeting_Date', 'meeting_place', 'photo',
                  'description']
