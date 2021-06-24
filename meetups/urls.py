from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:meetup_slug>', views.meetup_detail, name='detail')
]
