from django import forms

class SearchForm(forms.Form):
    """ This class is used to manage the form asociated with searching 
    workflows.
    """
    key = forms.CharField(label='Search Workflow', max_length=128)

    def is_valid(self):
        return True

class DownloadForm(forms.Form):

    def is_valid(self):
        return True