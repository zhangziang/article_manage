# encoding: utf-8

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import format_html


@python_2_unicode_compatible
class Publisher(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"姓名")

    def article_reading_count(self):
        reading_sum = 0
        articles = self.article_set.all()
        for i in articles:
            reading_sum += i.reading_count
        return reading_sum

    def publish_articles(self):
        html = u"<p>发布的文章</p><ol>"
        articles = self.article_set.all().order_by('-time')
        for i in articles:
            html += "<li><a href='"+reverse('admin:article_article_change', args=(i.pk,))+"'> " + i.title + "</a></li>"
        html += "</ol>"

        return format_html(html)

    class Meta:
        verbose_name = u"发布人"
        verbose_name_plural = u"发布人"

    def __str__(self):
        return self.name
