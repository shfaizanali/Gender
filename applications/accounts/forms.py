from django import forms
from account.forms import SignupForm
from django.utils.translation import ugettext_lazy as _
from django.forms import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()


class ModifiedSignUpForm(SignupForm):
    full_name = forms.CharField(max_length=60, label=_("Full Name"))
    file = forms.ImageField(required=False, label=_("Profile Pic"))

    def clean_username(self):
        username = super(ModifiedSignUpForm, self).clean_username()
        try:
            User.objects.get(username=username)
            raise ValidationError("Username already exists")
        except User.DoesNotExist:
            return username

