# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherPlot', '0002_auto_20160123_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='stations',
            field=models.ForeignKey(blank=True, null=True, to='weatherPlot.Station'),
        ),
    ]
