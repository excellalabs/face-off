# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_colleaguegraph_times_incorrect'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_custom_user',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='upload_img_file',
            field=s3direct.fields.S3DirectField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
