from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_professors, name='search_professors'),
    path('search-form/', views.search_form, name='search_form'),  # New route for search form

]
