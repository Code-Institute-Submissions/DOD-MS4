from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Developer, Language, Framework
from django.db.models import Q
from django.contrib import messages

# Create your views here.


def all_developers(request):
    """ Return the all the developers available on the app """

    developers = None
    developers = Developer.objects.all()
    query = None
    queries = None

    if request.GET:
        if 'framework' in request.GET:
            frameworks = request.GET['framework'].split(',')
            developers = developers.filter(framework__name__in=frameworks)
            frameworks = Framework.objects.filter(name__in=frameworks)

        if 'language' in request.GET:
            languages = request.GET['language'].split(',')
            developers = developers.filter(language__name__in=languages)
            languages = Language.objects.filter(name__in=languages)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('developers'))
            
            queries = Q(name__icontains=query) | Q(language__friendly_name__icontains=query) | Q(framework__friendly_name__icontains=query) | Q(spoken_language__name__icontains=query)
            developers = list(set(developers.filter(queries)))  # converting to a set then back to a list prevents object duplication for the search queries, .distict() could work similarly

    context = {
        'developers' : developers,
        'search_term': query,
    }

    return render(request, 'developers/developers.html', context)


def developer_detail(request, developer_id):
    """ Return the a requested developer to dev detail page """

    developer = get_object_or_404(Developer, pk=developer_id)

    context = {
        'developer' : developer,
    }

    return render(request, 'developers/developer_detail.html', context)