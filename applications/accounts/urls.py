from django.conf.urls import patterns, include, url
from .views import ModifiedSignUpView, ModifiedConfirmEmailView, ModifiedLoginView
from django.views.generic import TemplateView

partial_patterns = patterns(
    '',
    url(r'^account/signup/', ModifiedSignUpView.as_view(), name="account_signup"),
    url(r'^account/login/', ModifiedLoginView.as_view(), name="account_login"),
    url(r'^account/confirm_email/(?P<key>\w+)/$', ModifiedConfirmEmailView.as_view(), name="account_confirm_email"),
    url(r'^success/$', TemplateView.as_view(template_name="loginSuccess.html"), name="success_redirect"),
)

urlpatterns = patterns(
    '',
    url(r'^', include(partial_patterns, namespace='partials')),
    url(r'^account/', include('account.urls')),
)
