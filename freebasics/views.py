from django.views.generic import TemplateView
from django.conf import settings

from molo.profiles.views import RegistrationView, ProfilePasswordChangeView

from forms import FBRegistrationForm, ProfilePasswordChangeForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        blocks = [
            ('blocks/banners.html', settings.BLOCK_POSITION_BANNER),
            ('blocks/latest.html', settings.BLOCK_POSITION_LATEST),
            ('blocks/questions.html', settings.BLOCK_POSITION_QUESTIONS),
            ('blocks/sections.html', settings.BLOCK_POSITION_SECTIONS),
        ]
        blocks.sort(key=lambda tup: tup[1])
        context.update({
            'blocks': blocks,
            'self': self.request.site.root_page})
        return context


class FreeBasicsRegistrationView(RegistrationView):
    form_class = FBRegistrationForm


class FreeBasicsProfilePasswordChangeView(ProfilePasswordChangeView):
    form_class = ProfilePasswordChangeForm
