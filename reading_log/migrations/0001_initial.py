# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20151109_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=50)),
                ('article', models.ForeignKey(to='article.Article')),
            ],
        ),
    ]
