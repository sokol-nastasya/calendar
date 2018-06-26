from django import forms

class EntryForm(forms.Form):
	name = forms.CharField(max_length = 100)
	date = forms.DateTimeField()
	descriptions = forms.CharField(widget = forms.Textarea)