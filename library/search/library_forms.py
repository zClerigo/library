from django import forms

class LibraryForm(forms.Form):
   name = forms.CharField(max_length=100, required=True)
   author = forms.CharField(max_length=100, required=True)