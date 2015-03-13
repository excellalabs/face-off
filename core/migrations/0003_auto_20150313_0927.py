# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150311_1109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='globalmetrics',
            options={'verbose_name': 'Global Metric', 'verbose_name_plural': 'Global Metrics'},
        ),
        migrations.AlterModelOptions(
            name='mostknown',
            options={'verbose_name': 'Most known Colleague', 'verbose_name_plural': 'Most known Colleagues'},
        ),
        migrations.AlterModelOptions(
            name='usermetrics',
            options={'ordering': ['user__last_name'], 'verbose_name': 'User Metric', 'verbose_name_plural': 'User Metrics'},
        ),
    ]
