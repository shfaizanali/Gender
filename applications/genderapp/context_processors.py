from applications.genderapp.models import Language


def context_processor(request):
    data = dict()
    data['languages'] = Language.objects.all()
    return data