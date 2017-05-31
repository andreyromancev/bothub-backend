# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('user_id', models.PositiveIntegerField(db_index=True)),
                ('name', models.CharField(db_index=True, max_length=64)),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
