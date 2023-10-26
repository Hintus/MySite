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


def Profile(request):
    return render(request, 'groupsapp/Profile.html')


def show_profile(request, id):
    Profile = get_object_or_404(Profile, id=id)
    if Profile.user.id == request.user.id:
        return render(request, 'groupsapp/Profile.html', {'Profile': Profile})


class ShowProfilePage(DetailView):
    model = Profile
    template_name = 'groupsapp/Profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


# def AddGroup(request):
#     if request.method == 'POST':
#         form = AddGroupForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:
#         form = AddGroupForm()
#     return render(request, 'groupsapp/AddGroup.html', {'form': form})


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
