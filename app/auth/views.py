from django.contrib.auth.views import LoginView as UserLoginView
from .forms import AuthenticationForm


class LoginView(UserLoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
    redirect_authenticated_user = "/dashboard/"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


