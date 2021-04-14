from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_notes, name='view_notes'),
    path('add', views.add_note, name='add_note'),
    path('open/<int:document_id>', views.open_note, name='open_note'),
    path('edit/<int:document_id>', views.edit_note, name='edit_note'),
    path('delete/<int:document_id>', views.delete_note, name='delete_note'),
]
