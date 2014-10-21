from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Course)
admin.site.register(Language)
admin.site.register(CourseProgress)
admin.site.register(Subscribe)
admin.site.register(Word)