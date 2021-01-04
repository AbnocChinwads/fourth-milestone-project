from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes, name='notes'),
    path('add-notes/', views.add_notes, name='add-notes'),
    path('open-notes/', views.open_notes, name='open-notes'),
]
