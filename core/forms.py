from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, ButtonHolder, Button, Submit, Field, HTML, Div
from crispy_forms.bootstrap import FormActions
from core.models import Suggestions, UserProfile

class UserAuthenticationForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout()

        self.helper.layout.append(Div('username'))
        self.helper.layout.append(Div('password'))

        self.helper.layout.append(FormActions(
            Submit('Submit', 'Submit', css_class='btn btn-primary pull-right'),
            HTML("<button id=\"close\" type=\"button\" class=\"btn btn-default pull-right\" data-dismiss=\"modal\">Close</button>"),
        ))

    def save(self):
        user = super(UserAuthenticationForm, self)
        user.save()
        return user

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
       # self.fields['upload_img_file'] = forms.URLField(widget=S3DirectWidget(dest='img'))
        self.fields['upload_img_file'].label = 'Profile Image'
        self.fields['upload_img_file'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

        self.helper.layout.append(FormActions(
            Submit('Submit', 'Submit'),
        ))

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'password', 'upload_img_file')


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestions
        fields = ('first_name', 'last_name', 'email', 'suggestion')


class ResultForm(forms.Form):
    score = forms.IntegerField(widget=forms.HiddenInput())
    answer_id = forms.IntegerField(widget=forms.HiddenInput())
    results = forms.CharField(widget=forms.HiddenInput())
    correct = forms.CharField(widget=forms.HiddenInput())
    mode = forms.CharField(widget=forms.HiddenInput())
