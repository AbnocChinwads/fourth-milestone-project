from django.shortcuts import render

from .models import Document


def notes(request):
    """
    A view to show all campaign notes for the user,
    including sorting and search queries
    """

    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    context = {
        'docid': docid,
        'documents': documents,
    }

    return render(request, 'notes.html', context)


def add_notes(request):
    """
    A view to show all campaign notes for the user,
    including sorting and search queries
    """

    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    context = {
        'docid': docid,
        'documents': documents,
    }

    return render(request, 'add-notes.html', context)


def open_notes(request):
    """
    A view to show all campaign notes for the user,
    including sorting and search queries
    """

    docid = int(request.GET.get('docid'))
    documents = Document.objects.all()

    context = {
        'docid': docid,
        'documents': documents,
    }

    return render(request, 'open-notes.html', context)
