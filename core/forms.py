from django import forms
from core.models import Suggestions


class SuggestionForm(forms.ModelForm):

    class Meta:
        model = Suggestions