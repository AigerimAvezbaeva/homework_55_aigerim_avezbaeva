from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from to_do_app.models import ToDoParagraph


def to_do_view(request: WSGIRequest):
    paragraphs = ToDoParagraph.objects.exclude(is_deleted=True)
    context = {
        'paragraphs': paragraphs
    }
    return render(request, 'to_do_index.html', context=context)
