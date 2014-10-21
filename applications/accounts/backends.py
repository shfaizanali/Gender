from django.http.response import Http404
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model, login
from social.pipeline.partial import partial


User = get_user_model()


@partial
def api_backend(strategy, backend, uid, *args, **kwargs):
    if backend.name == 'facebook' or backend.name == 'google-oauth2':
        try:
            details = kwargs['details']
            if details['fullname'] != '':
                fullname = details['fullname']
            else:
                fullname = details['first_name'] + " " + details['last_name']

            if details['email'] == '':
                email = uid + "@facebook.com"
            else:
                email = details['email']
            if 'username' in details:
                user_id = details['username']
            else:
                user_id = uid

            response = kwargs['response']
            if 'image' in response:
                avatar = response['image']['url']
            else:
                avatar = ""

            user, created = User.objects.get_or_create(username=user_id, full_name=fullname, email=email)
            user.social_image = avatar
            if created:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                user.set_unusable_password()
            user.save()

            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(strategy.request, user)
            return HttpResponseRedirect('/#/profile')

        except Exception as exception:
            print exception

            # authenticated_user = authenticate(user_id=user_id, uid=uid, details=details, avatar=avatar)
            # login(strategy.request, authenticated_user)
            # return {'user': authenticated_user, 'provider': backend.name}
        #    return HttpResponseRedirect('/#/profile')
        #except Exception as exception:
        #    raise exception

    raise Http404
