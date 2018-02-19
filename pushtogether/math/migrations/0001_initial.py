# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-15 21:54
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CLUSTERS', 'CLUSTERS')], max_length=20)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('STARTED', 'STARTED'), ('FINISHED', 'FINISHED'), ('FAILED', 'FAILED')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('argument', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=3), size=None)),
                ('result', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
        ),
    ]