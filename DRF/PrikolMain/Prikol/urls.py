from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Prikol import settings
from groupsapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Groups', groups_page, name='groups'),
    path('minion/', minion, name='minion'),
    path('', main_page, name='Main_page'),
    path('Market/', market_page, name='market'),
    path('Login/', LoginUser.as_view(), name='login'),
    path('Logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('Profile/', Profile, name='profile'),
    path('group/<slug:group_slug>', show_group, name='group_profile_url'),
    path('GroupCreationForm/', GroupCreationForm, name='add_group'),
    path('GroupCreationForm/CreateGroup', CreateGroup, name='CreateGroup'),
    path('group/<str:group_name>', add_member, name='add_member')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
