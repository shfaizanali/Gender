from django.shortcuts import render
from django.views.generic import View
from applications.accounts.forms import ModifiedSignUpForm
# Create your views here.

from django.views.generic import FormView
from .forms import ProfileForm
from .models import Course, Language, Subscribe, WORD_STATUS
from django.http import HttpResponse
import json
from django.core import serializers
from django.contrib.auth.decorators import login_required


class ProfileView(FormView):
    form_class = ProfileForm
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        context['subscriptions'] = self.request.user.subscribed_user.all()
        for subscription in context['subscriptions']:
            try:
                course = Course.objects.filter(language=subscription.subscribed_language)[0]
                total_words = course.course_word.count()
                known_words = course.course.filter(status='known').count()
                subscription.progress = (float(known_words)/float(total_words))*100
            except Exception as e:
                context['subscriptions'] = context['subscriptions'].exclude(id=subscription.id)

        return context

@login_required
def get_all_languages(request):
    languages = serializers.serialize("json", Language.objects.all())
    return HttpResponse(languages, content_type="application/json")


@login_required
def subscribe_for_languages(request):
    languages = json.loads(request.body)
    for language in languages['fields']:
        try:
            Subscribe.objects.create(subscribed_user=request.user, subscribed_language_id=int(language))
        except Exception as e:
            continue
    return HttpResponse("hello")