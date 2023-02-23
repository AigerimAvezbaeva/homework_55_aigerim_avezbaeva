from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from to_do_app.models import ToDoParagraph
from to_do_app.forms import ToDoForm


def add_paragraph(request: WSGIRequest):
    if request.method == 'GET':
        form = ToDoForm()
        return render(request, 'add_paragraph.html', context={'form': form})
    form = ToDoForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'add_paragraph.html', context={'form': form})
    else:
        paragraph = ToDoParagraph.objects.create(**form.cleaned_data)
        return redirect('paragraph_detail', pk=paragraph.pk)


def paragraph_view(request, pk):
    paragraph = get_object_or_404(ToDoParagraph, pk=pk)
    return render(request, 'to_do_paragraph.html', context={
        'paragraph': paragraph
    })


def update_toDo(request, pk):
    errors = {}
    paragraph = get_object_or_404(ToDoParagraph, pk=pk)
    form = ToDoForm(instance=paragraph)
    print(form)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=paragraph)
        if not request.POST.get('title'):
            errors['title'] = 'Данное поле обязательно к заполнению'
        paragraph.title = request.POST.get('title')
        paragraph.description = request.POST.get('description')
        paragraph.status = request.POST.get('status')
        paragraph.completion_date = request.POST.get('completion_date')
        if errors:
            return render(request, 'to_do_update.html', context={
                'paragraph': paragraph,
                'form': form,
                'errors': errors
            })
        form.save()
        return redirect('to_do_paragraph.html', pk=paragraph.pk)
    return render(request, 'to_do_update.html', context={
        'paragraph': paragraph,
        'form': form
    })


def delete_toDo(request, pk):
    paragraph = get_object_or_404(ToDoParagraph, pk=pk)
    return render(request, 'tdp_confirm_delete.html', context={
        'paragraph': paragraph
    })


def tdp_confirm_delete(request, pk):
    paragraph = get_object_or_404(ToDoParagraph, pk=pk)
    paragraph.delete()
    return redirect('index')
