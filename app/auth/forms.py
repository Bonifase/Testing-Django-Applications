from django.contrib.auth.forms import UserCreationForm, AuthenticationForm as AuthForm
from django import forms


class AuthenticationForm(AuthForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["placeholder"] = "Password"
        self.fields["password"].widget.attrs["class"] = "form-control"


class UserProfileForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    first_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )

        # super(UserProfileForm, self).__init__(*args, **kwargs)
        # self.fields["username"].widget.attrs["placeholder"] = "Username"
        # self.fields["username"].widget.attrs["class"] = "form-control"
        # self.fields["password"].widget.attrs["placeholder"] = "Password"
        # self.fields["password"].widget.attrs["class"] = "form-control"
        # self.fields["first_name"].widget.attrs["placeholder"] = "First Name"
        # self.fields["first_name"].widget.attrs["class"] = "form-control"
        # self.fields["last_name"].widget.attrs["placeholder"] = "Last Name"
        # self.fields["last_name"].widget.attrs["class"] = "form-control"