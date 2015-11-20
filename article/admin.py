# encoding: utf-8
from django.contrib import admin
from models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'publisher', 'time', 'reading_count', 'content')
    readonly_fields = ('time', 'reading_count')
    list_display = ('title', 'time', 'reading_count', 'publisher')
