import json
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from account.views import SignupView, ConfirmEmailView, LoginView
from .forms import ModifiedSignUpForm

User = get_user_model()


class ModifiedSignUpView(SignupView):
    form_class = ModifiedSignUpForm

    def create_user(self, form, commit=True, **kwargs):
        user = super(ModifiedSignUpView, self).create_user(form=form, commit=False,  **kwargs)
        user.full_name = form.cleaned_data.get("full_name")
        user.avatar = form.cleaned_data.get("file")
        if commit:
            user.save()
        return user

    def form_invalid(self, form):
        if self.request.is_ajax():
            data = dict()
            data["errors"] = form.errors
            data["success"] = False
            return HttpResponse(json.dumps(data), content_type="application/json", status=400)

        return super(ModifiedSignUpView, self).form_invalid(form)


class ModifiedConfirmEmailView(ConfirmEmailView):

    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm()
        self.after_confirmation(confirmation)
        return super(ModifiedConfirmEmailView, self).get(args, kwargs)

    def after_confirmation(self, confirmation):
        user = confirmation.email_address.user
        user.is_active = True
        user.save()


class ModifiedLoginView(LoginView):
    def form_invalid(self, form):
        if self.request.is_ajax():
            data = dict()
            data["errors"] = form.errors
            data["success"] = False
            return HttpResponse(json.dumps(data), content_type="application/json", status=400)

        return super(ModifiedLoginView, self).form_invalid(form)
