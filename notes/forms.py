from django.forms import ModelForm
from .models import Document


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'content']


# Creating a form to add a document
form = DocumentForm()


# Creating a form to change an existing document
# document = Document.objects.get(pk=1)
# form = DocumentForm(instance=document)
