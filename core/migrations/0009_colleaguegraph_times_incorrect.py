# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_colleaguegraph_yammer_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='colleaguegraph',
            name='times_incorrect',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
