# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherPlot', '0003_auto_20160123_0415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='stations',
        ),
        migrations.AddField(
            model_name='station',
            name='user_profile',
            field=models.ManyToManyField(null=True, to='weatherPlot.UserProfile', blank=True),
        ),
    ]
