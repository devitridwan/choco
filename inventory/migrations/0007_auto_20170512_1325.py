# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_pengeluaran_harga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemasukan',
            name='total_harga',
            field=models.IntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='pengeluaran',
            name='harga',
            field=models.IntegerField(),
        ),
    ]
