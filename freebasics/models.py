from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, PageChooserPanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class LogoPage(Page):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    logo_link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Optional page to which the banner will link to')
    )

    parent_page_types = ['core.Main']
    subpage_types = []

LogoPage.content_panels = [
    FieldPanel('title', classname='full title'),
    ImageChooserPanel('logo'),
    PageChooserPanel('logo_link_page'),
]
