# encoding: utf-8

from django.views.generic import TemplateView

from .models import Article
from reading_log.models import ReadingLog

class ArticleView(TemplateView):

    template_name = 'article.html'

    def get(self, request, uid):

        uid = int(uid)
        try:
            article = Article.objects.get(pk=uid)

            client_ip = request.META['REMOTE_ADDR']
            ReadingLog.objects.get_or_create(ip=client_ip, article=article)
        except Article.DoesNotExist:
            article = False

        context = {'article': article}
        return self.render_to_response(context)
