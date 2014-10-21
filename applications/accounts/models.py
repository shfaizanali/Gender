from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class GenderUserManager(BaseUserManager):

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, is_active=True, **extra_fields):
        """
        Creates and saves a User with the given email, email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError(_('The given email must be set'))

        email = super(GenderUserManager, self).normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=is_active,
                          is_superuser=is_superuser, last_login=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, is_staff=False, is_superuser=False, is_active=True,
                                 **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, is_staff=True, is_superuser=True, is_active=True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30,  unique=True, db_index=True, verbose_name=_('username'))
    email = models.EmailField(max_length=254, unique=True, db_index=True, verbose_name=_('email'))
    full_name = models.CharField(_('Full name'), max_length=60, blank=True, null=True, default="")
    avatar = models.ImageField(_('Profile'), upload_to='avatars', default="avatars/default/default_profile.jpg")
    social_image = models.URLField(_("Social"), default="", blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['username']

    USERNAME_FIELD = 'email'

    objects = GenderUserManager()

    class Meta:
        verbose_name = _('Gender User')
        verbose_name_plural = _('Gender Users')

    def __unicode__(self):
        return self.email

    def get_short_name(self):
        if self.full_name:
            return self.full_name.split(' ')[0]
        else:
            return ""
