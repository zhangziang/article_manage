# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20151109_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
    ]
