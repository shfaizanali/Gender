# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genderapp', '0003_auto_20141018_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionprogress',
            name='subscription',
        ),
        migrations.DeleteModel(
            name='SubscriptionProgress',
        ),
        migrations.RenameField(
            model_name='courseprogress',
            old_name='Course',
            new_name='course',
        ),
    ]
