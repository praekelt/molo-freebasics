from django.test import TestCase
from django.test.client import Client
from molo.core.tests.base import MoloTestCaseMixin
from freebasics.views import HomeView


class BlocksTestCase(TestCase, MoloTestCaseMixin):

    def setUp(self):
        self.mk_main()
        self.client = Client()

    def test_block_ordering(self):
        with self.settings(BANNER_BLOCK_POSITION=4,
                           LATEST_BLOCK_POSITION=3,
                           QUESTIONS_BLOCK_POSITION=2,
                           SECTIONS_BLOCK_POSITION=1):
            self.client.login(username='tester', password='tester')
            home = HomeView()
            context = home.get_context_data()
            self.assertEquals(context['blocks'][0], (
                'blocks/sections.html', 1))
            self.assertEquals(context['blocks'][1], (
                'blocks/questions.html', 2))
            self.assertEquals(context['blocks'][2], ('blocks/latest.html', 3))
            self.assertEquals(context['blocks'][3], ('blocks/banners.html', 4))
