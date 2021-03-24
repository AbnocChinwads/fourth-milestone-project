from django.shortcuts import render, redirect, get_object_or_404

from .models import Document
from .forms import DocumentForm


def view_notes(request):
    """
    A view to show all campaign notes for the user,
    including sorting and search queries
    """
    docid = request.POST.get('docid')
    documents = Document.objects.all()

    context = {
        'docid': docid,
        'documents': documents,
    }

    return render(request, 'notes.html', context)

# Create


def add_note(request):
    """ A view to create a new document """
    if request.method == 'POST':
        form = DocumentForm(request.POST.get)

        if form.is_valid:
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            document = Document(title=title, content=content)
            document.save()
    else:
        form = Document()

    return render(request, 'add-notes.html', {'form': form})

# Read


def open_note(request, docid):
    """ A view to show the currently open document """
    docid = get_object_or_404(Document, pk=docid)
    documents = Document.objects.all(pk=docid)

    context = {
        'docid': docid,
        'documents': documents,
    }

    return render(request, 'open-notes.html', context)

# Update


def update_note(request):
    """ A view to update the currently open document """
    if request.method == 'POST':
        form = DocumentForm(request.POST.get)

        if form.is_valid:
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            document = Document(title=title, content=content)
            document.save()
    else:
        form = Document()

    return redirect(request, 'notes.html', {'form': form})

# Delete


def delete_note(request, docid):
    """ A view to delete the currently open document """
    document = get_object_or_404(Document, pk=docid)
    document.delete()

    return redirect('notes.html')
