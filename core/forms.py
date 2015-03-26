from django import forms

from core.models import Suggestions


class SuggestionForm(forms.ModelForm):

    class Meta:
        model = Suggestions
        fields = ('first_name', 'last_name', 'email', 'suggestion')

class ResultForm(forms.Form):
    score = forms.IntegerField(widget=forms.HiddenInput())
    cardIndex = forms.IntegerField(widget=forms.HiddenInput())
    results = forms.CharField(widget=forms.HiddenInput())

