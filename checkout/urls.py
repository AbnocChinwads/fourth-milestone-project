from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('create-sub', views.create_sub, name='create sub'),
    path('complete', views.complete, name='complete'),
    path('cancel', views.cancel, name='cancel'),
]
