# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-21 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0093_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('name', models.CharField(blank=True, max_length=8)),
                ('bool', models.BooleanField(default=True)),
                ('number', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
