from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='start'),
    path('name', views.get_name, name='name'),
]