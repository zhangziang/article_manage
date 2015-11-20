# encoding: utf-8

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from publisher.models import Publisher

from froala_editor.fields import FroalaField


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=400, verbose_name=u'标题')
    time = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    publisher = models.ForeignKey(to=Publisher)
    content = FroalaField(null=True, blank=True, verbose_name=u'正文')

    @property
    def reading_count(self):
        return len(self.readinglog_set.all())

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

    def __str__(self):
        return self.title
