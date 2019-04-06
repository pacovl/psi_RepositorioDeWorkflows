from django.shortcuts import render
from data.models import Workflow, Category
from find.forms import SearchForm
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json

def workflow_list(request, category_slug=None):
    """This function lists all Workflows if no second argument is provided.
        In any other case, it looks for the workflows associated to 
        the specified category and returns them.
    Author: Emilio Cuesta Fernandez

    Args:
        request: the request object calling this view.
        category_slug: the slug of a categorie if selected, none by default.

    Returns:
        Render of the html page to show.
    """

    result = True
    error = ""
    category = None
    workflows = []


    if category_slug == None:
        # By default (and if no 2nd arguments is provided)
        # category will be None

        # Workflows will include all wfs as no filter was given
        workflows = Workflow.objects.all()

    else:
        # Otherwise, it takes the category object from the slug.
        match = Category.objects.filter(slug  = category_slug)
        if match.exists():
            category = match[0]

            # And workflows are also filtered by this cat
            match = Workflow.objects.filter(category = category)
            if match.exists():
                workflows = list(match)
            else: 
                # Query failed, we return the message below
                result = False
                error = "{} category doesnt own any workflow".format(category_slug)
        else: 
            # Query failed, we return the message below
            result = False
            error = "{} category does not exist!".format(category_slug)

       

    categories = Category.objects.all()

    # Variables for the pagination of the worflows
    page = request.GET.get('page', 1)
    paginator = Paginator(workflows, 8)

    try:
        workflows = paginator.page(page)
    except PageNotAnInteger:
        workflows = paginator.page(1)
    except EmptyPage:
        workflows = paginator.page(paginator.num_pages)


    _dict = {'category': category,  # category associated to category_slug
            'categories': categories,  # list with all categories
                                    # usefull to repaint the category
                                    # menu
            'workflows': workflows,    # subset of all workflows associated to category 
                                    # category_slug
            'result': result,           # False if no workflow satisfices the query
            'error': error,              # message to display if results == False
            'form':  SearchForm()
    }

    return render(request, 'find/list.html', _dict)


def workflow_detail(request, id, slug):
    """This view shows the details of the indicated workflow.
    Author: Emilio Cuesta Fernandez

    Args:
        request: the request that is calling this view.
        id: identifier of the selected workflow.
        slug: slug of the selected workflow.

    Returns:
        The html page with the information of the workflow.
    """

    error = ""
    workflow = None
    result = True

    match = Workflow.objects.filter(id = id, slug = slug)

    if match.exists():
        workflow = match[0]
    else: 
        # Query failed, we return the message below
        result = False
        error = "Workflow with id {} and slug {} does not exists".format(id, slug)

    _dict = {}
    _dict['result'] = result      # False if no workflow satisfices the query
    _dict['workflow'] = workflow  # workflow with id = id   
    _dict['error'] = error        # message to display if results == False
    _dict['form'] = SearchForm()


    return render(request, 'find/detail.html', _dict)


def workflow_search(request):
    """This view show the details of a searched workflow if it exists.
    Author: Emilio Cuesta Fernandez

    Args:
        request: the request that is calling this view, which should be POST and has
        a key attribute asociated with the input text.

    Returns:
        the html page with the details of the workflow or a warning if it does not exist.
    """

    if request.method == 'POST':
        
        form = SearchForm(request.POST)

        if form.is_valid():
            key = request.POST['key']

            result = True
            workflow = None
            error = ""
            match = Workflow.objects.filter(slug = key)
            if match.exists():
                workflow = match[0]
            else: 
                # Query failed, we return the message below
                result = False
                error = "Workflow with name or slug '{}'  does not exists".format(key)
            #query that returns the workflow with name = name
            _dict = {}
            _dict['result'] = result      # False if no workflow satisfices the query
            _dict['workflow'] = workflow  # workflow with name = name
            _dict['error'] = error        # message to display if results == False
            _dict['form'] = SearchForm()
            return render(request, 'find/detail.html', _dict)


    return "You shouldnt be here!"