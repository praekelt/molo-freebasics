from django.template import Library
from django.conf import settings

register = Library()


@register.template_tag('custom_css.html', takes_context=True)
def custom_css(context):
    styles = {
        "body-background-color": settings.CUSTOM_CSS_BASE_BACKGROUND_COLOR,
        "body-font-family": settings.CUSTOM_CSS_BODY_FONT_FAMILY,
        "block-background-color": settings.CUSTOM_CSS_BLOCK_BACKGROUND_COLOR,
        "block-font-family": settings.CUSTOM_CSS_BLOCK_FONT_FAMILY,
        "text-transform": settings.CUSTOM_CSS_BLOCK_TEXT_TRANSFORM,
        "accent-1": settings.CUSTOM_CSS_ACCENT_1,
        "accent-2": settings.CUSTOM_CSS_ACCENT_2
    }
    return {'styles': styles}
