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
    path('Profile/<int:Profile_user_id>', show_profile, name='show_profile_url'),
    path('group/<slug:group_slug>', show_group, name='group_profile_url')
    # path('AddGroup/', AddGroup, name='add_group')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
