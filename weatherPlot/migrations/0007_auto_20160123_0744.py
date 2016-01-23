# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherPlot', '0006_datapoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='humidity_tag',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='humidity_value',
            field=models.DecimalField(null=True, decimal_places=3, max_digits=5, blank=True),
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='temperature_tag',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='temperature_value',
            field=models.DecimalField(null=True, decimal_places=3, max_digits=5, blank=True),
        ),
    ]
