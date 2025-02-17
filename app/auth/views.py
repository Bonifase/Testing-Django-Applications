from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as UserLoginView
from django.views.generic import UpdateView, TemplateView, DetailView

from tasks.models import Task

from .forms import AuthenticationForm, UserProfileForm


class LoginView(UserLoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

class UserProfileView(DetailView):
    # form_class = UserProfileForm
    template_name = "registration/edit_profile.html"


    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.id).all()

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['title'] = 'Update Profile'
        context['form'] =  UserProfileForm()
        return context


def get_user_profile(request):
    user = User.objects.get(pk=request.user.id)
    tasks = Task.objects.filter(owner=user).order_by('due_date')
    return render(
        request,
        template_name='registration/user_profile.html',
        context={"user":user, "title": request.user.username, "total_tasks":len(tasks)}
    )
