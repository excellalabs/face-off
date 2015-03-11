"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from core.models import UserMetrics, UserProfile,User, GlobalMetrics,MostKnown


#The classes defined below are placeholders for future test
#after business logic has been implemented

class UserMetricsTest(UserMetrics):
    pass

class UserProfileTest(UserProfile):
    pass

class UserTest(User):
    pass

class GlobalMetricsTest(GlobalMetrics):
    pass

class MostKnownTest(MostKnown):
    pass


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
