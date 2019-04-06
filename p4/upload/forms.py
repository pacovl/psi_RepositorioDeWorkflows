from django import forms
from data.models import Category, Workflow
from django.db import models
from django.forms import ModelForm

class UploadForm(ModelForm):
    """ This class is used to manage the form asociated with 
    uploading workflows.
    """
    json = forms.FileField(label='Workflow File', required = True)


    class Meta:
        model = Workflow 
        fields = ['name', 'category', 'keywords', 'description', 'versionInit']
        widgets = {'description' : forms.Textarea}
