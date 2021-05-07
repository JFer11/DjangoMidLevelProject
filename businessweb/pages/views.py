from django.shortcuts import render, get_object_or_404
from .models import Page


def page(request, page_id, page_slug):
    # This page_slug parameter is redundant, however, it could help  SEO page positioning.
    page_object = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page.html', {'page': page_object})
