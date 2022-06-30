from django.contrib.auth.forms import UserCreationForm, AuthenticationForm as AuthForm
from django.contrib.auth.models import User


class AuthenticationForm(AuthForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["placeholder"] = "Password"
        self.fields["password"].widget.attrs["class"] = "form-control"