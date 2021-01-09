from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Developer, Language, Framework
from django.db.models import Q
from django.contrib import messages
from .forms import DeveloperForm

# Create your views here.


def all_developers(request):
    """ Return the all the developers available on the app """

    developers = None
    developers = Developer.objects.all()
    query = None
    queries = None
    sort = None
    direction = None
    redirect_url = request.GET.get('redirect_url')

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            developers = developers.order_by(sortkey)

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
                return redirect(redirect_url)
            
            queries = Q(name__icontains=query) | Q(language__friendly_name__icontains=query) | Q(framework__friendly_name__icontains=query) | Q(spoken_language__name__icontains=query)
            developers = list(set(developers.filter(queries)))  # converting to a set then back to a list prevents object duplication for the search queries, .distict() could work similarly

    current_sorting = f'{sort}_{direction}'

    if 'framework' in request.GET:
        context = {
            'developers': developers,
            'search_term': query,
            'current_selection': frameworks,
            'current_sorting': current_sorting,
        }
    elif 'language' in request.GET:
        context = {
            'developers': developers,
            'search_term': query,
            'current_selection': languages,
            'current_sorting': current_sorting,
        }
    else:
        context = {
            'developers': developers,
            'search_term': query,
            'current_sorting': current_sorting,
        }

    return render(request, 'developers/developers.html', context)


def developer_detail(request, developer_id):
    """ Return the a requested developer to dev detail page """

    developer = get_object_or_404(Developer, pk=developer_id)

    context = {
        'developer' : developer,
    }

    return render(request, 'developers/developer_detail.html', context)

    
def add_developer(request):
    """ Add a developer to the store """
    if request.method == 'POST':
        form = DeveloperForm(request.POST, request.FILES)
        if form.is_valid():
            developer = form.save()
            messages.success(request, 'Successfully added developer!')
            return redirect(reverse('developer_detail', args=[developer.id]))
        else:
            messages.error(request, 'Failed to add developer. Please ensure the form is valid.')
    else:
        form = DeveloperForm()

    template = 'developers/add_developer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_developer(request, developer_id):
    """ Edit a developer in the store """
    developer = get_object_or_404(Developer, pk=developer_id)
    if request.method == 'POST':
        form = DeveloperForm(request.POST, request.FILES, instance=developer)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated developer: {developer.name}')
            return redirect(reverse('developer_detail', args=[developer.id]))
        else:
            messages.error(request, f'Failed to update developer: {developer.name}. Please ensure the form is valid.')
    else:
        form = DeveloperForm(instance=developer)
        messages.info(request, f'You are editing {developer.name}')

    template = 'developers/edit_developer.html'
    context = {
        'form': form,
        'developer': developer,
    }

    return render(request, template, context)


def delete_developer(request, developer_id):
    """ Delete a developer from the store """
    developer = get_object_or_404(Developer, pk=developer_id)
    if request.method == 'POST':
        developer = get_object_or_404(Developer, pk=developer_id)
        context = {
            'developer': developer,
            'confirm_delete': True,
        }
        return render(request, 'developers/developer_detail.html', context)
    else:
        developer.delete()
        messages.success(request, 'developer deleted!')
        return redirect(reverse('developers'))