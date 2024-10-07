from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_search_form, name='home'),  # Root URL redirects to search form
    path('search/', views.search_professors, name='search_professors'),
    path('search-form/', views.search_form, name='search_form'),
]
