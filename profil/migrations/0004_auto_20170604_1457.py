# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0003_profile_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='group',
            field=models.CharField(blank=True, editable=False, max_length=15),
        ),
    ]