from django import forms
from data.models import Workflow, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
    help_text="Please enter the category name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    created = forms.DateField(widget=forms.HiddenInput(), required=False)
    tooltip = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class WorkflowForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
    help_text="Please enter workflow name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    downloads = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    created = forms.DateField(widget=forms.HiddenInput(), required=False)
    category = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Workflow
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('description', 'versionInit', 'client_ip','keywords', 'json')
       