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
            'next': reverse('molo.profiles:registration_done')
        })
        self.assertRedirects(response, reverse(
            'molo.profiles:registration_done'))
        self.assertEquals(User.objects.all().count(), 1)
        self.assertEquals(User.objects.all()[0].username, 'testing')
