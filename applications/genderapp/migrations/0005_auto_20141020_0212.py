# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genderapp', '0004_auto_20141020_0135'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscribe',
            unique_together=set([('subscribed_language', 'subscribed_user')]),
        ),
    ]
