from django.shortcuts import render, redirect

from .models import Document


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


def add_notes(request):
    """
    A view to save the newly created document to the database
    """
    if request.method == 'POST':
        title = request.POST.get('document_title')
        content = request.POST.get('document_content')
        Document.objects.create(title=title, content=content)

        return redirect('view_notes')
    return render(request, 'notes/add_notes.html')
