from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

User = settings.AUTH_USER_MODEL

POSSIBLE_GENDERS = (
    ('masculine', 'Masculine'),
    ('feminine', 'Feminine'),
    ('neutral', 'Neutral'),
)

WORD_STATUS = (
    ('seen', 'seen'),
    ('known', 'known'),
    ('skipped', 'skipped'),
)


class Language(models.Model):
    language = models.CharField(max_length=50, verbose_name=_("Language"))
    subscription_cost = models.FloatField(verbose_name=_("Subscription Cost"))
    flag = models.ImageField(verbose_name=_("Flag"), upload_to='flags', default="flags/default/default_flag.png")

    def __unicode__(self):
        return self.language


class Subscribe(models.Model):
    subscribed_language = models.ForeignKey(Language, related_name="subscribed_language",
                                            verbose_name=_("Subscribed Language"))
    subscribed_user = models.ForeignKey(User, related_name="subscribed_user", verbose_name=_("Subscribed User"))

    def __unicode__(self):
        return self.subscribed_language.language

    class Meta:
        unique_together = ("subscribed_language", "subscribed_user")


class Course(models.Model):
    language = models.ForeignKey(Language, related_name="course_of")
    course_name = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Course Name"))

    def __unicode__(self):
        return self.language.language


class Word(models.Model):
    Course = models.ForeignKey(Course, related_name="course_word", verbose_name=_("Course"))
    word = models.CharField(max_length=100, verbose_name=_("word"))
    gender = models.CharField(max_length=20, choices=POSSIBLE_GENDERS, verbose_name=_('Gender'))

    def __unicode__(self):
        return self.word


class CourseProgress(models.Model):
    course = models.ForeignKey(Course, related_name="course", verbose_name=_("Course"))
    user = models.ForeignKey(User, related_name="user", verbose_name=_("User"))
    word = models.ForeignKey(Word, related_name="course_word", verbose_name=_("Word"))
    status = models.CharField(max_length=20, choices=WORD_STATUS, verbose_name=_("Word Status"))
    user_answer = models.CharField(max_length=20, choices=POSSIBLE_GENDERS, verbose_name=_("User Answer"))

    def __unicode__(self):
        return self.course.course_name


