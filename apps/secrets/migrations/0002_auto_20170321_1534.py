# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='secret',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='secrets.Secret'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='secrets.User'),
        ),
    ]
