from django import forms
from events.models import Event
"""
A simple form for creating a new event, which is a simple description
field and that is it.
"""

class EventForm(forms.ModelForm):
	description = forms.CharField(max_length=350,widget=forms.Textarea)
	title = forms.CharField(max_length=50)
	class Meta:
		model = Event
		fields = ('title','description',)