from django import forms

class AnnotatedDocumentCreationForm(forms.Form):
    title = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'class':'form-control'}))
    # slug = forms.CharField(required=False,
    #         widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(
            widget=forms.Textarea(attrs={'class':'form-control'}))
