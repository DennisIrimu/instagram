# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-22 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20180621_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_follows',
            field=models.ManyToManyField(blank=True, related_name='follows', to='insta.Profile'),
        ),
    ]
