from django import forms
from django.contrib.auth import get_user_model

from allauth.account import forms as account_forms


class LoginForm(account_forms.LoginForm):
    class Meta:
        field_order = ['login', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs.update({
            'class': 'required email form-control',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'required form-control',
        })


class ProfileForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
            'mobile_number',
            'city',
        )

    def __init__(self, *args, **kwargs):

        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['email'].disabled = True

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'First Name'
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Last Name'
        })

        self.fields['city'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'City'
        })

        self.fields['mobile_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Mobile Number'
        })


class UserSignupForm(account_forms.SignupForm):
    first_name = forms.CharField(max_length=155)
    last_name = forms.CharField(max_length=155)

    class Meta:
        fields = [
            'first_name', 'last_name', 'email', 'password1', 'password2'
        ]

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'required form-control',
            'placeholder': 'First Name',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'required form-control',
            'placeholder': 'Last Name',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'required email form-control',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'required form-control',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'required form-control',
        })

    def custom_signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class ResetPasswordForm(account_forms.ResetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class': 'required email form-control',
        })


class ChangePasswordForm(account_forms.ChangePasswordForm):

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['oldpassword'].widget.attrs.update({
            'class': 'required form-control',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'required form-control',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'required form-control',
        })
