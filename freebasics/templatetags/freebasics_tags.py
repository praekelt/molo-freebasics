from django.template import Library
from django.conf import settings

register = Library()


@register.template_tag('custom_css.html', takes_context=True)
def custom_css(context):
    styles = {
        "body-background-color": settings.CUSTOM_BODY_BACKGROUND_COLOR,
        "body-font-color": settings.CUSTOM_BODY_FONT_COLOR,
        "body-font-family": settings.CUSTOM_BODY_FONT,
        "accent-1": settings.CUSTOM_ACCENT_1,
        "accent-2": settings.CUSTOM_ACCENT_2
    }
    return {'styles': styles}
