from core.forms import SuggestionForm, ResultForm
from django.test import TestCase

class FormTests(TestCase):

    #Test all SuggestionForm data
    def test_all_suggestion_fields(self):
        form = SuggestionForm({
            'first_name': 'Sean',
            'last_name': 'Lewis',
            'email': 'sean.lewis@excella.com',
            'suggestion': 'Hello world',
        })

        self.assertEqual(form.is_valid(), True)

    #Test first_name is required
    def test_suggestion_first_name_required(self):
        form = SuggestionForm({
            'last_name': 'Lewis',
            'email': 'sean.lewis@excella.com',
            'suggestion': 'Hello world',
        })

        self.assertEqual(form.is_valid(), False)

    #Test last_name is required
    def test_suggestion_last_name_required(self):
        form = SuggestionForm({
            'first_name': 'Sean',
            'email': 'sean.lewis@excella.com',
            'suggestion': 'Hello world',
        })

        self.assertEqual(form.is_valid(), False)

    #Test email is required
    def test_suggestion_email_required(self):
        form = SuggestionForm({
            'first_name': 'Sean',
            'last_name': 'Lewis',
            'suggestion': 'Hello world',
        })

        self.assertEqual(form.is_valid(), False)

    #Test suggestion is required
    def test_suggestion_suggestion_required(self):
        form = SuggestionForm({
            'first_name': 'Sean',
            'last_name': 'Lewis',
            'email': 'sean.lewis@excella.com',

        })

        self.assertEqual(form.is_valid(), False)

    #Test all ResultsForm fields
    def test_all_results_fields(self):
        form = ResultForm({
            'score': 1,
            'cardIndex': 3,
            'results': 'hello',
        })

        self.assertEqual(form.is_valid(), True)

    #Test score is required
    def test_results_score_required(self):
        form = ResultForm({
            'cardIndex': 3,
            'results': 'hello',
        })

        self.assertEqual(form.is_valid(), False)

    #Test cardIndex is required
    def test_results_cardIndex_required(self):
        form = ResultForm({
            'score': 1,
            'results': 'hello',
        })

        self.assertEqual(form.is_valid(), False)

    #Test results are required
    def test_results_results_required(self):
        form = ResultForm({
            'score': 1,
            'cardIndex': 3,
        })

        self.assertEqual(form.is_valid(), False)