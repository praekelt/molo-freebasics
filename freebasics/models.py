from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from django.db import models


@register_setting
class SiteSettings(BaseSetting):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('logo'),
    ]
