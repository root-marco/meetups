from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:meetup_slug>', views.meetup_details)
]
