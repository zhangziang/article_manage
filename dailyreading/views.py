# encoding: utf-8

from django.views.generic import TemplateView

from article.models import Article


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, page="1"):

        page = int(page)

        if page == 0:
            page += 1

        page_amount = 10

        begain_index = (page-1) * page_amount
        end_index = page * page_amount

        article_list = Article.objects.all().order_by('-time')[begain_index: end_index]
        article_amount = len(Article.objects.all())

        if end_index >= article_amount:
            next_page = False
        else:
            next_page = page + 1

        if page > 1:
            front_page = page - 1
        else:
            front_page = False

        context = {'article_list': article_list,
                   'front_page': front_page,
                   'next_page': next_page
                   }

        return self.render_to_response(context)

