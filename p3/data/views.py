from django.shortcuts import render

from django.http import HttpResponse

from data.models import Category
from data.models import Workflow

from data.forms import CategoryForm
from data.forms import WorkflowForm


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!

    return render(request, 'data/list.html')

    # category_list = Category.objects.all()
    # workflow_list = Workflow.objects.all()

    # context_dict = {'categories': category_list,
    #                 'workflows': workflow_list}


    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    # return render(request, 'data/index.html', context=context_dict)  


def about(request):
	context_dict = {'names': "Emilio and Francisco"}
	return render(request, 'data/about.html', context=context_dict)


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated workflows.
        # Note that filter() will return a list of workflow objects or an empty list
        workflows = Workflow.objects.filter(category=category)
        # Adds our results list to the template context under name workflows.
        context_dict['workflows'] = workflows
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['workflows'] = None
    # Go render the response and return it to the client.
    return render(request, 'data/category.html', context_dict)

def show_workflow(request, workflow_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        workflow = Workflow.objects.get(slug=workflow_name_slug)
        context_dict['workflow'] = workflow

    except Workflow.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['workflow'] = None
    # Go render the response and return it to the client.
    return render(request, 'data/workflow.html', context_dict)


def add_category(request):
    form = CategoryForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
    # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index workflow
            # Then we can direct the user back to the index workflow.
            return index(request)
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'data/add_category.html', {'form': form})


def add_workflow(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    form = WorkflowForm()
    if request.method == 'POST':
        form = WorkflowForm(request.POST)
        if form.is_valid():
            if category:
                workflow = form.save(commit=False)
                workflow.client_ip = request.META['REMOTE_ADDR']
                workflow.views = 0
                workflow.save()
                workflow.category.add(category)

            return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form':form, 'category': category}
    return render(request, 'data/add_workflow.html', context_dict)
