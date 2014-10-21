# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genderapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='flag',
            field=models.ImageField(default=b'flags/default/default_flag.jpg', upload_to=b'flags', verbose_name='Flag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseprogress',
            name='status',
            field=models.CharField(max_length=20, verbose_name='Word Status', choices=[(b'seen', b'seen'), (b'known', b'known'), (b'skipped', b'skipped')]),
        ),
        migrations.AlterField(
            model_name='word',
            name='Course',
            field=models.ForeignKey(related_name=b'course_word', verbose_name='Course', to='genderapp.Course'),
        ),
    ]
