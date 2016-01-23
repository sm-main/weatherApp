# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherPlot', '0005_auto_20160123_0429'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateField()),
                ('temperature_value', models.DecimalField(max_digits=5, decimal_places=3)),
                ('temperature_tag', models.CharField(max_length=500)),
                ('humidity_value', models.DecimalField(max_digits=5, decimal_places=3)),
                ('humidity_tag', models.CharField(max_length=500)),
                ('user_profile', models.ForeignKey(to='weatherPlot.UserProfile')),
            ],
        ),
    ]
