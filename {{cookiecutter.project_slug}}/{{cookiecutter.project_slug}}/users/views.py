from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin

from django.http import HttpResponse

from django.views import View
from django.views.generic.edit import UpdateView

from django.core.urlresolvers import reverse

from user import forms


class UpdateProfile(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = forms.ProfileForm
    success_message = "Profile updated."

    def get_object(self):
        return self.model.objects.get(pk=self.request.user.pk)

    def get_success_url(self):
        return reverse('edit_profile')


class ValidateEmail(View):

    def get(self, request, *args, **kwargs):
        email = request.GET.get('email').strip()

        valid = email is not None and get_user_model().objects.filter(
            email__iexact=email
        ).exists()

        if valid:
            return HttpResponse('false')

        return HttpResponse('true')


class CheckEmail(View):

    def get(self, request, *args, **kwargs):
        email = request.GET.get('email').strip()
        if not email:
            email = request.GET.get('username').strip()

        checked = email is not None and get_user_model().objects.filter(
            email__iexact=email
        ).exists()
        if checked:
            return HttpResponse('true')

        return HttpResponse('false')
