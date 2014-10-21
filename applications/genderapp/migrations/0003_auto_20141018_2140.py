# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genderapp', '0002_auto_20141018_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='flag',
            field=models.ImageField(default=b'flags/default/default_flag.png', upload_to=b'flags', verbose_name='Flag'),
        ),
    ]
