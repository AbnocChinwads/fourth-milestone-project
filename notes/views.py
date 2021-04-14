from django.shortcuts import render, redirect, get_object_or_404

from .models import Document
from .forms import DocumentForm


def view_notes(request):
    """
    A view to show all campaign notes for the user,
    including sorting and search queries
    """
    documents = Document.objects.all()

    context = {
        'documents': documents,
    }

    return render(request, 'notes/notes.html', context)


def add_note(request):
    """
    A view to save the newly created document to the database
    """
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_notes')
    form = DocumentForm()
    context = {
        'form': form
    }
    return render(request, 'notes/add_note.html', context)


def open_note(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    """if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('view_notes')"""
    form = DocumentForm(instance=document)
    context = {
        'form': form
    }
    return render(request, 'notes/open_note.html', context)


def edit_note(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('view_notes')
    form = DocumentForm(instance=document)
    context = {
        'form': form
    }
    return render(request, 'notes/edit_note.html', context)


def delete_note(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.delete()
    return redirect('view_notes')
