# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_userprofile_network'),
    ]

    operations = [
        migrations.AddField(
            model_name='colleaguegraph',
            name='yammer_url',
            field=models.URLField(default=datetime.datetime(2015, 4, 3, 13, 58, 6, 871749, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
