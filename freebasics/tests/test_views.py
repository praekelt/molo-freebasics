from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User


class RegistrationViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_registration_with_password(self):
        self.assertEquals(User.objects.all().count(), 0)
        response = self.client.post(reverse('user_register'), {
            'username': 'testing',
            'password': 'testing',
        })
        self.assertRedirects(response, reverse(
            'molo.profiles:user_register'))
        self.assertEquals(User.objects.all().count(), 1)
        self.assertEquals(User.objects.all()[0].username, 'testing')
