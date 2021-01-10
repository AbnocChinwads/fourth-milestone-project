from django.shortcuts import render, redirect, HttpResponseRedirect, reverse

from .models import Document


def view_or_open_notes(request):
    """
    A view to show all campaign notes for the user,
    including sorting and search queries
    """

    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if docid > 0:
            document = Document.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.save()

            return redirect('notes')
        else:
            document = Document.objects.create(title=title, content=content)

            return HttpResponseRedirect(reverse('notes'))

    if docid > 0:
        document = Document.objects.get(pk=docid)
    else:
        document = ''

    context = {
        'docid': docid,
        'documents': documents,
        'document': document,
    }

    if docid != 0:
        return render(request, 'open-notes.html', context)
    else:
        return render(request, 'notes.html', context)


"""def add_notes(request):

    A view to show all campaign notes for the user,
    including sorting and search queries


    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    context = {
        'docid': docid,
        'documents': documents,
    }

    return render(request, 'add-notes.html', context)"""


def delete_note(request, docid):
    document = Document.objects.get(pk=docid)
    document.delete()

    return redirect('notes')
