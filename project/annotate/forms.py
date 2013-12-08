from django import forms

class AnnotatedDocumentCreationForm(forms.Form):
    title = forms.CharField(required=False)
    slug = forms.CharField(required=False)
    content = forms.CharField(widget=forms.Textarea)
