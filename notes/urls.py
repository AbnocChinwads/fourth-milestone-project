from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_or_open_notes, name='notes'),
    path('add-notes/', views.view_or_open_notes, name='add-notes'),
    path('open-notes/', views.view_or_open_notes, name='open-notes'),
    path('edit-note/<int:docid>/', views.view_or_open_notes, name='edit-note'),
    path('delete-note/<int:docid>/', views.delete_note, name='delete-note'),
]
