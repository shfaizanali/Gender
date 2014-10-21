# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=50, null=True, verbose_name='Course Name', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=20, verbose_name='Word Status', choices=[(0, b'seen'), (1, b'known'), (2, b'skipped')])),
                ('user_answer', models.CharField(max_length=20, verbose_name='User Answer', choices=[(b'masculine', b'Masculine'), (b'feminine', b'Feminine'), (b'neutral', b'Neutral')])),
                ('Course', models.ForeignKey(related_name=b'course', verbose_name='Course', to='genderapp.Course')),
                ('user', models.ForeignKey(related_name=b'user', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=50, verbose_name='Language')),
                ('subscription_cost', models.FloatField(verbose_name='Subscription Cost')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subscribed_language', models.ForeignKey(related_name=b'subscribed_language', verbose_name='Subscribed Language', to='genderapp.Language')),
                ('subscribed_user', models.ForeignKey(related_name=b'subscribed_user', verbose_name='Subscribed User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubscriptionProgress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('progress', models.FloatField(default=0, verbose_name='progress')),
                ('words_seen', models.IntegerField(default=0, verbose_name='Seen')),
                ('known_words', models.IntegerField(default=0, verbose_name='Known')),
                ('skipped_words', models.IntegerField(default=0, verbose_name='Skipped')),
                ('subscription', models.ForeignKey(related_name=b'subscription', to='genderapp.Subscribe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=100, verbose_name='word')),
                ('gender', models.CharField(max_length=20, verbose_name='Gender', choices=[(b'masculine', b'Masculine'), (b'feminine', b'Feminine'), (b'neutral', b'Neutral')])),
                ('Course', models.ForeignKey(related_name=b'test_word', verbose_name='Course', to='genderapp.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='courseprogress',
            name='word',
            field=models.ForeignKey(related_name=b'course_word', verbose_name='Word', to='genderapp.Word'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.ForeignKey(related_name=b'course_of', to='genderapp.Language'),
            preserve_default=True,
        ),
    ]
