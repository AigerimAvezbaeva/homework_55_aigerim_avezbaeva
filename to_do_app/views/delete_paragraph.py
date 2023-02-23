from django.shortcuts import render, get_object_or_404

from to_do_app.models import ToDoParagraph


def delete_paragraph(request, pk):
    paragraph = get_object_or_404(ToDoParagraph, pk=pk)
    paragraph.delete()
    paragraphs = ToDoParagraph.objects.all()
    context = {
        'paragraphs': paragraphs
    }
    return render(request, 'to_do_index.html', context=context)

