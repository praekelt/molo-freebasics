from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

from molo.core.models import ArticlePage
from wagtail.wagtailsearch.models import Query


def search(request, results_per_page=10):
    search_query = request.GET.get('q', None)
    page = request.GET.get('p', 1)

    if search_query:
        results = ArticlePage.objects.live().search(search_query)
        Query.get(search_query).add_hit()
    else:
        results = ArticlePage.objects.none()

    paginator = Paginator(results, results_per_page)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search/search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
        'results': results,
    })


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        blocks = [
            ('blocks/banners.html', settings.BANNER_BLOCK_POSITION),
            ('blocks/latest.html', settings.LATEST_BLOCK_POSITION),
            ('blocks/questions.html', settings.QUESTIONS_BLOCK_POSITION),
            ('blocks/sections.html', settings.SECTIONS_BLOCK_POSITION),
        ]
        blocks.sort(key=lambda tup: tup[1])
        context.update({'blocks': blocks})
        return context
