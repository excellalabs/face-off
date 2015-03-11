# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalMetrics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('network', models.CharField(unique=True, max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MostKnown',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('most_known_colleague', models.CharField(max_length=200, blank=True)),
                ('date_time', models.DateField(verbose_name=b'Timestamp')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserMetrics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('times_won', models.IntegerField(default=0, blank=True)),
                ('times_known', models.IntegerField(default=0, blank=True)),
                ('user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'ordering': ['user__last_name'],
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='metrics',
            name='user',
        ),
        migrations.DeleteModel(
            name='Metrics',
        ),
        migrations.AddField(
            model_name='globalmetrics',
            name='most_known',
            field=models.ForeignKey(to='core.MostKnown'),
            preserve_default=True,
        ),
    ]
