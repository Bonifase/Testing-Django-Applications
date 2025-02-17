from django.contrib.auth.views import LogoutView
from django.urls import re_path

from .views import (
    LoginView,
    get_user_profile,
    UserProfileView
)


urlpatterns = [
    re_path(r'login', LoginView.as_view(), name='login'),
    re_path(r'logout', LogoutView.as_view(), name='logout'),
    re_path(r'profile', get_user_profile, name='profile'),
    re_path(r'profile/(?P<pk>.*)/', UserProfileView.as_view(), name='edit_profile'),
]