from django.urls import path, include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from .auth.views import LoginView, get_user_profile, UserProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', get_user_profile, name='profile'),
    path('accounts/profile/<slug:pk>/', UserProfileView.as_view(), name='edit_profile'),
    path('', include("tasks.urls")),
]
urlpatterns += static(settings.STATIC_URL)
