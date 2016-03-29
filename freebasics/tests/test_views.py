from django.core.urlresolvers import reverse
from django.test import TestCase, Client


class RegistrationViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register_view_invalid_form(self):
        # NOTE: empty form submission
        response = self.client.post(reverse('user_register'), {
            'username': 'testing',
            'password': 'testing',
        })
        print response
        self.assertRedirects(response, reverse('user_register'))
