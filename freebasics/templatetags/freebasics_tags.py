from django.template import Library
from django.conf import settings

register = Library()


@register.inclusion_tag('custom_css.html', takes_context=True)
def custom_css(context):
    styles = {
        "body_background_color": settings.CUSTOM_CSS_BASE_BACKGROUND_COLOR,
        "body_font_family": settings.CUSTOM_CSS_BODY_FONT_FAMILY,
        "block_background_color": settings.CUSTOM_CSS_BLOCK_BACKGROUND_COLOR,
        "block_font_family": settings.CUSTOM_CSS_BLOCK_FONT_FAMILY,
        "text_transform": settings.CUSTOM_CSS_BLOCK_TEXT_TRANSFORM,
        "accent_1": settings.CUSTOM_CSS_ACCENT_1,
        "accent_2": settings.CUSTOM_CSS_ACCENT_2
    }
    return styles


@register.simple_tag(takes_context=True)
def get_site_name(context):
    return settings.SITE_NAME


@register.assignment_tag(takes_context=True)
def load_sections(context):
    request = context['request']
    locale_code = context.get('locale_code')
    qs = request.site.root_page.specific.sections()
    return [a.get_translation_for(locale_code) or a for a in qs]
