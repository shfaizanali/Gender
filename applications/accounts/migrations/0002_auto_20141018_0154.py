# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=b'avatars/default/default_profile.jpg', upload_to=b'avatars', verbose_name='Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='social_image',
            field=models.URLField(default=b'', null=True, verbose_name='Social', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(default=b'', max_length=60, null=True, verbose_name='Full name', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(unique=True, max_length=30, verbose_name='username', db_index=True),
        ),
    ]
