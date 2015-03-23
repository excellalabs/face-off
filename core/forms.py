from django import forms


class ResultForm(forms.Form):
    score = forms.IntegerField(widget=forms.HiddenInput())
    cardIndex = forms.IntegerField(widget=forms.HiddenInput())
    results = forms.CharField(widget=forms.HiddenInput())