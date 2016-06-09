# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-06 20:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0086_get_requester_ratings_fn_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagerecipient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messagerecipient',
            name='delivered_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='messagerecipient',
            name='read_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='messagerecipient',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 6, 20, 14, 50, 357747, tzinfo=utc)),
            preserve_default=False,
        ),
    ]