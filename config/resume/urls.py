from django.urls import path
from .views import index,AboutListView
urlpatterns = [
    path('', index,name='index'),
    path('about', AboutListView.as_view(),name='about'),
]
