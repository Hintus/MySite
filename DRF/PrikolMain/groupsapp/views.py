import transliterate
from transliterate import slugify
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import authenticate, logout, login
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from groupsapp.models import *
from groupsapp.forms import *


# Create your views here.

def groups_page(request):
    all_groups = MyGroups.objects.all()

    return render(request, 'groupsapp/Groups.html', {'data': all_groups})


def minion(request):  # САМОЕ ВАЖНОЕ, ЧТО ЕСТЬ НА САЙТЕ, НЕ УДАЛЯТЬ
    return render(request, 'groupsapp/Minion.html')


def main_page(request):
    return render(request, 'groupsapp/Main_Page.html')


def market_page(request):
    all_groups = MyGroups.objects.all()

    all_goods = Goods.objects.all()

    return render(request, 'groupsapp/Market.html', {'goods': all_goods, "groups": all_groups})


class RegisterUser(CreateView):
    from_class = UserCreationForm
    success_url = reverse_lazy('main_page')


def show_group(request, group_slug):
    group = get_object_or_404(MyGroups, slug=group_slug)

    return render(request, 'groupsapp/Group_profile.html', {'group': group})


def add_member(request, group_name):
    group = MyGroups.objects.get(name=group_name)
    New = User.objects.get(username = request.user.username)
    group.members.add(New)
    return render(request, 'groupsapp/Group_profile.html', {'group': group})


def Profile(request):
    return render(request, 'groupsapp/Profile.html')

# ДОДЕЛАТЬ!!!
def Edit_Profile(request):
    request.user.username = request.POST['name']
    request.user.username = request.POST['name']
    request.user.username = request.POST['name']
    request.user.username = request.POST['name']
    return render(request, 'groupsapp/Profile.html')

def GroupCreationForm(request):
    return render(request, 'groupsapp/GroupCreationForm.html')

def CreateGroup(request):
    Group_name = request.POST['group name']
    kirill = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    find_kirill = [x for x in kirill if x in Group_name.lower()]
    if find_kirill == []:
        Group_Slug = Group_name
    else:
        Group_Slug = slugify(Group_name)
    
    Group_place = request.POST['meeting place']
    Group_Date = request.POST.get('meeting date', '2023-10-26 09:16:39')
    Group_Discription = request.POST['discription']
    Group_Pas = request.POST['Password']

    if MyGroups.objects.filter(name=Group_name).exists():
        return render(request, 'groupsapp/GroupCreationForm.html')
    else:
        new_group = MyGroups.objects.create(name=Group_name,
                                            meeting_place=Group_place,
                                            meeting_Date=Group_Date,
                                            slug = Group_Slug,
                                            description=Group_Discription,
                                            password = Group_Pas)
        new_group.save()

        group = get_object_or_404(MyGroups, slug=new_group.slug)

        return render(request, 'groupsapp/Group_profile.html', {'group': group})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'groupsapp/register.html'
    success_url = reverse_lazy('Main_page')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('Main_page')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'groupsapp/login.html'

    def get_success_url(self):
        return reverse_lazy('Main_page')


def logout_user(request):
    logout(request)
    return redirect('Main_page')