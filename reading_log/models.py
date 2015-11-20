# encoding: utf-8

from django.db import models
from article.models import Article


class ReadingLog(models.Model):
    ip = models.CharField(max_length=50)
    article = models.ForeignKey(to=Article)

    def __str__(self):
        return self.ip + ' ' + self.article.title
