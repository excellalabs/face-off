from django.test import TestCase
from core.models import Suggestions, UserMetrics


class FormTests(TestCase):

    def create_suggestion(self, first_name="Sean", last_name="Lewis", email="sean.lewis@excella.com", suggestion="Hello World"):
        return Suggestions.objects.create(first_name=first_name, last_name=last_name, email=email, suggestion=suggestion
                                          )

    def test_suggestion_creation(self):
        suggestion = self.create_suggestion()
        self.assertTrue(isinstance(suggestion, Suggestions))
        self.assertEqual(suggestion.__unicode__(), suggestion.suggestion)

#Create test case for usermetrics __unicode__
'''
class UserMetricsTest(TestCase):

    def create_user_metric(self, user='John', times_won=4, times_known=5):
        return UserMetrics.objects.create(user=user, times_won=times_won, times_known=times_known)

    def test_user_metric_creation(self):
        user_metric = self.create_user_metric()
        self.assertTrue(isinstance(user_metric, UserMetrics))
        self.assertEqual(user_metric.__unicode__(),user_metric.user)
'''