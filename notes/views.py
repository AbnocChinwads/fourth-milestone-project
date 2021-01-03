from django.shortcuts import render

# Create your views here.


def notes(request):
    """ A view to open the notes page """
    return render(request, 'notes.html')
