# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0001_initial'),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4', auto_created=True)),
                ('title', models.CharField(max_length=400, verbose_name='\u6807\u9898')),
                ('content', ckeditor.fields.RichTextField(null=True, verbose_name='\u6b63\u6587', blank=True)),
                ('publisher', models.ForeignKey(to='publisher.Publisher')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.RemoveField(
            model_name='articlemodel',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='ArticleModel',
        ),
    ]
