from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_notes, name='view_notes'),
    path('add', views.add_notes, name='add_notes'),
]
