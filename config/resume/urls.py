from django.urls import path
from .views import index,ContactCreateView
urlpatterns = [
    path('', index,name='index'),
    path('contact', ContactCreateView.as_view(),name='contact'),
]
