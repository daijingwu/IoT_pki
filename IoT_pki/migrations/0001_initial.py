# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 14:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cert_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(blank=True, max_length=2)),
                ('state_or_province_name', models.CharField(blank=True, max_length=50)),
                ('locality_name', models.CharField(blank=True, max_length=50)),
                ('organization_name', models.CharField(blank=True, max_length=50)),
                ('organization_unit_name', models.CharField(blank=True, max_length=50)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
                ('user_id', models.CharField(blank=True, max_length=50)),
                ('dns_name', models.CharField(blank=True, max_length=250)),
                ('common_name', models.CharField(max_length=50)),
                ('dn_qualifier', models.CharField(blank=True, max_length=250)),
                ('not_valid_after', models.DateTimeField(default=datetime.datetime(2017, 9, 9, 14, 46, 2, 768501, tzinfo=utc))),
                ('approved', models.BooleanField(default=False)),
                ('issued', models.BooleanField(default=False)),
                ('request_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('token', models.CharField(db_index=True, default='N8GIN6FK5UELY1B1PQSG5HWJMNIJVH', max_length=50)),
                ('is_ca', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=2)),
                ('state_or_province_name', models.CharField(blank=True, max_length=50)),
                ('locality_name', models.CharField(blank=True, max_length=50)),
                ('organization_name', models.CharField(blank=True, max_length=50)),
                ('organization_unit_name', models.CharField(blank=True, max_length=50)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
                ('user_id', models.CharField(blank=True, max_length=50)),
                ('dns_name', models.CharField(blank=True, max_length=250)),
                ('common_name', models.CharField(blank=True, max_length=50)),
                ('dn_qualifier', models.CharField(blank=True, max_length=250)),
                ('not_valid_before', models.DateTimeField()),
                ('not_valid_after', models.DateTimeField()),
                ('serial_number', models.CharField(db_index=True, max_length=250)),
                ('revoked', models.BooleanField(default=False)),
                ('is_ca', models.BooleanField(db_index=True, default=False)),
                ('issuer_serial_number', models.IntegerField()),
            ],
        ),
    ]