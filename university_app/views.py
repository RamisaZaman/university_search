from django.shortcuts import render
from .models import Professor, University

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
