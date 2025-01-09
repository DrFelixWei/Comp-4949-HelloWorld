# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, felixPageView, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('felix/', felixPageView, name='felix'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
