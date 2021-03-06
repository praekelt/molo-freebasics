from django.test import TestCase, RequestFactory
from molo.core.tests.base import MoloTestCaseMixin
from freebasics.views import HomeView
from freebasics.templatetags import freebasics_tags


class EnvTestCase(TestCase, MoloTestCaseMixin):

    def setUp(self):
        self.mk_main()

    def test_block_ordering(self):
        with self.settings(BLOCK_POSITION_BANNER=1,
                           BLOCK_POSITION_LATEST=2,
                           BLOCK_POSITION_QUESTIONS=3,
                           BLOCK_POSITION_SURVEYS=4,
                           BLOCK_POSITION_TOPIC_OF_THE_DAY=5,
                           BLOCK_POSITION_YOURWORDS=6,
                           BLOCK_POSITION_SECTIONS=7):
            factory = RequestFactory()
            request = factory.get('/')
            request.site = self.site
            home = HomeView()
            home.request = request
            context = home.get_context_data()
            print context
            self.assertEquals(context['blocks'][0], (
                'blocks/banners.html', 1))
            self.assertEquals(context['blocks'][1], (
                'blocks/latest.html', 2))
            self.assertEquals(context['blocks'][2], (
                'blocks/questions.html', 3))
            self.assertEquals(context['blocks'][3], ('blocks/surveys.html', 4))
            self.assertEquals(context['blocks'][4], (
                'blocks/topic_of_the_day.html', 5))
            self.assertEquals(context['blocks'][5], (
                'blocks/yourwords.html', 6))
            self.assertEquals(context['blocks'][6], (
                'blocks/sections.html', 7))

    def test_css_vars(self):
        with self.settings(CUSTOM_CSS_BLOCK_TEXT_TRANSFORM="lowercase",
                           CUSTOM_CSS_ACCENT_2="red"):
            styles = freebasics_tags.custom_css(context='')
            self.assertEquals(styles['accent_2'], 'red')
            self.assertEquals(styles['text_transform'], 'lowercase')

    def test_custom_css(self):
        response = self.client.get('/')
        self.assertContains(response, 'Free Basics Custom CSS')
        self.assertContains(response, '.custom-template-container__content')
        self.assertContains(response, '.heading')
        self.assertContains(response, '.article-list__heading')
