# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carro',
            old_name='name',
            new_name='nome',
        ),
    ]
