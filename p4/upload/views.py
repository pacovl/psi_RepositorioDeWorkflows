from django.shortcuts import render
from data.models import Workflow, Category
from upload.forms import UploadForm
from django.template.defaultfilters import slugify
from django import forms
from find.forms import SearchForm, DownloadForm
from django.http import HttpResponse

import json

def add_workflow(request):
    """
    Author: Emilio Cuesta Fernandez

    Args:
        request: the request object calling this view.

    Returns:
        Render of the html page to show.
    """

    _dict = {}
    
    if request.method == 'POST':
        
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid() == True:
            
            wf = form.save()
            # get json content
            workflowFile = form.cleaned_data['json']
            # decode html coded  binary  data
            filedata = workflowFile.read().decode('utf-8')
            # modify  object  json  value  in  form so  it
            # has  'plain'  text  instead  of  encoded
            form.instance.json = filedata

            wf.save()

            _dict = {}
            _dict['result'] = True      # False if no workflow satisfices the query
            _dict['wf'] = wf  # workflow with id = id   
            _dict['error'] = "error"        # message to display if results == False
            _dict['form'] = SearchForm()
            _dict['downloadform'] = DownloadForm()

            return render(request, 'upload/success.html', _dict)
        
        return HttpResponse("You shoulnt be here!")

    else:
        _dict['form'] = UploadForm()  # category associated to category_slug
        return render(request, 'upload/add_wf.html', _dict)