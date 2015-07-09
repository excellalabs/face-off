from django.test import TestCase
import django.core.mail
from django.core.urlresolvers import reverse
from mock import patch

@patch('django.core.mail.send_mail')
class ViewTest(TestCase):

    # TODO - Investigate: Splitting the three tests below into different test functions
    #        results in the last one failing due to call_count = 0 instead of 1.

    def test_ajax_suggestion(self, mock_send_mail):
        mock_send_mail.return_value = True

        # 1 Non-Ajax post
        resp = self.client.post(reverse('core:ajax_suggestion'), {'first_name':'John', 'last_name':'Doe', 'suggestion':'suggestion content', 'email':'john.doe@example.com'})

        self.assertContains(resp, 'Service unavailable')
        self.assertEqual(mock_send_mail.call_count, 0)

        # 2 Ajax post with bad form data

        # XMLHttpRequest satisfies request.is_ajax()
        resp = self.client.post(reverse('core:ajax_suggestion'), {'last_name':'Doe', 'suggestion':'suggestion content', 'email':'john.doe@example.com'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertContains(resp, 'Invalid Data!')
        self.assertEqual(mock_send_mail.call_count, 0)

        # 3 Valid Ajax Post

        # Override settings.ADMINS
        test_emails = ['email1@test.com', 'email2@test.com']
        test_admins = (('example1', test_emails[0]), ('example2', test_emails[1]))

        with self.settings(ADMINS=test_admins):
            # XMLHttpRequest satisfies request.is_ajax()
            resp = self.client.post(reverse('core:ajax_suggestion'), {'first_name':'John', 'last_name':'Doe', 'suggestion':'suggestion content', 'email':'john.doe@example.com'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertContains(resp, 'Thank you for your suggestion!')
        self.assertEqual(mock_send_mail.call_count, 1)
        mock_send_mail.assert_called_once_with('New Suggestion for Face-Off from John Doe',
                                               'suggestion content',
                                               'john.doe@example.com',
                                               test_emails)
