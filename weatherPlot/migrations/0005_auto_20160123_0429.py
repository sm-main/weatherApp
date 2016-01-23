# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherPlot', '0004_auto_20160123_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='user_profile',
            field=models.ManyToManyField(to='weatherPlot.UserProfile', blank=True),
        ),
    ]
