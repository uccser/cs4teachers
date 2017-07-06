# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 13:26
from __future__ import unicode_literals

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_auto_20170706_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(default='0.0,0.0', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=django_google_maps.fields.AddressField(max_length=200),
        ),
    ]
