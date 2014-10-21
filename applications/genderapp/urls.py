from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import ProfileView, get_all_languages, subscribe_for_languages
from applications.accounts.views import ModifiedSignUpView

partial_patterns = patterns(
    '',
    url(r'^home/$', TemplateView.as_view(template_name="home.html"), name="Home"),
    url(r'^profile/$', ProfileView.as_view(), name="Profile"),
)

urlpatterns = patterns(
    '',
    url(r'^', include(partial_patterns, namespace='partials')),
    url(r'^languages/$', get_all_languages, name='languages'),
    url(r'^subscribe/languages/$', subscribe_for_languages, name='subscribe')
)
