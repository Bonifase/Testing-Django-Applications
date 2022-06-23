from django.contrib.auth.views import LoginView as UserLoginView


class LoginView(UserLoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


