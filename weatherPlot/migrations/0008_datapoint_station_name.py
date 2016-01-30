# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherPlot', '0007_auto_20160123_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='station_name',
            field=models.CharField(max_length=40, default='Delhi'),
            preserve_default=False,
        ),
    ]
