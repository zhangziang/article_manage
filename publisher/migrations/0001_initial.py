# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u59d3\u540d')),
            ],
            options={
                'verbose_name': '\u53d1\u5e03\u4eba',
                'verbose_name_plural': '\u53d1\u5e03\u4eba',
            },
        ),
    ]
