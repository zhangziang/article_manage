# encoding: utf-8

from django.conf.urls import url

from views import ArticleView


urlpatterns = [
    url(r'(?P<uid>[0-9]+)/$', ArticleView.as_view(), name='article'),
]
