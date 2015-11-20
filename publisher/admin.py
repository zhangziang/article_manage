# encoding: utf-8

from django.contrib import admin
from models import Publisher

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    readonly_fields = ('article_reading_count', 'publish_articles')
