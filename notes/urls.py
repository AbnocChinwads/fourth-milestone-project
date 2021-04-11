from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_notes, name='view_notes'),
    path('add', views.add_note, name='add_note'),
    path('edit/<int:document_id>', views.edit_note, name='edit_note'),
]
