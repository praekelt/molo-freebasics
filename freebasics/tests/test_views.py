from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from molo.core.tests.base import MoloTestCaseMixin

from molo.core.models import SiteLanguage


class RegistrationViewTest(TestCase, MoloTestCaseMixin):

    def setUp(self):
        self.client = Client()
        # Creates Main language
        self.english = SiteLanguage.objects.create(
            locale='en',
        )
        # Creates translation Language
        self.french = SiteLanguage.objects.create(
            locale='fr',
        )
        self.mk_main()

        # Creates a section under the index page
        self.english_section = self.mk_section(
            self.section_index, title='English section')

    def test_registration_with_password(self):

        self.assertEquals(User.objects.all().count(), 0)
        response = self.client.post(reverse('user_register'), {
            'username': 'testing',
            'password': 'testing',
            'terms_and_conditions': True,
            'next': reverse('molo.profiles:registration_done')
        })
        self.assertRedirects(response, reverse(
            'molo.profiles:registration_done'))
        self.assertEquals(User.objects.all().count(), 1)
        self.assertEquals(User.objects.all()[0].username, 'testing')
