from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_notes, name='notes'),
    path('add-notes/', views.add_note, name='add-notes'),
    path('open-notes/<int:docid>/', views.open_note, name='open-notes'),
    path('edit-note/', views.update_note, name='edit-note'),
    path('delete-note/', views.delete_note, name='delete-note'),
]
