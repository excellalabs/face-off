# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_suggestions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColleagueGraph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yammer_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('img_url', models.URLField(blank=True)),
                ('times_correct', models.IntegerField(default=0, blank=True)),
                ('user', models.ForeignKey(related_name='user_colleague_graph', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__id'],
                'verbose_name': 'Graph of Known Colleagues',
                'verbose_name_plural': 'Graphs of Known Colleagues',
            },
            bases=(models.Model,),
        ),
    ]
