from django.shortcuts import render, redirect

from .models import Document


def view_notes(request, docid):
    """
    A view to show all campaign notes for the user,
    including sorting and search queries
    """
    docid = request.GET.get('docid')
    documents = Document.objects.all()

    context = {
        'docid': docid,
        'documents': documents,
    }

    return render(request, 'notes.html', context)

# Create


def add_note(request):
    """ A view to create a new document """
    docid = request.GET.get('docid')
    documents = Document.objects.all()
    """ document input from webpage """
    # document.save()

    context = {
        'docid': docid,
        'documents': documents,
        # 'document': document,
    }

    return render(request, 'add-notes.html', context)

# Read


def open_note(request, docid):
    """ A view to show the currently open document """
    docid = request.GET.get('docid')
    documents = Document.objects.all(pk=docid)

    context = {
        'docid': docid,
        'documents': documents,
    }

    return render(request, 'open-notes.html', context)

# Update


def update_note():
    """ A view to update the currently open document """
    return redirect('notes')

# Delete


def delete_note(request, docid):
    """ A view to delete the currently open document """
    document = Document.objects.get(pk=docid)
    document.delete()

    return redirect('notes')
