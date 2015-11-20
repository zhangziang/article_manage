# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20151109_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=froala_editor.fields.FroalaField(null=True, verbose_name='\u6b63\u6587', blank=True),
        ),
    ]
