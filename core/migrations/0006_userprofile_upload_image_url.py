# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_colleaguegraph'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='upload_image_url',
            field=models.URLField(default=datetime.datetime(2015, 3, 27, 15, 49, 23, 397619, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
