# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_userprofile_upload_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='network',
            field=models.CharField(default='excella', max_length=50),
            preserve_default=False,
        ),
    ]
