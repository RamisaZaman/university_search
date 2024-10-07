from django.http import HttpResponse  # For returning basic responses
from django.shortcuts import render, redirect  # For rendering templates and redirects
from .models import Professor, University  # Import your models


def home(request):
    return HttpResponse("Welcome to the University Search App! Visit /search-form to begin.")


# Existing views
def search_professors(request):
    # Get search filters from the request (e.g., country, degree type, etc.)
    country = request.GET.get('country')
    research_area = request.GET.get('research_area')

    # Get all professors, and filter based on search criteria if provided
    professors = Professor.objects.all()

    if country:
        professors = professors.filter(university__country=country)
    if research_area:
        professors = professors.filter(research_area__icontains=research_area)

    return render(request, 'search_results.html', {'professors': professors})

def search_form(request):
    return render(request, 'search_form.html')

# New view for root URL redirection
def redirect_to_search_form(request):
    return redirect('search_form')  # Redirects to search form page
