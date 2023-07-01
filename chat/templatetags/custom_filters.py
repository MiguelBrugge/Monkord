from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

#Line Breaks
@register.filter
def preserve_linebreaks(value):
    return mark_safe(value.replace('\n', '<br>'))

#Custom text appearance
@register.filter
def filter_text(value):
    bold_pattern = r'\*\*(.*?)\*\*'
    italic_pattern = r'\*(.*?)\*'
    h1_pattern = r'\#(.*?)\#'
    h2_pattern = r'\#\#(.*?)\#\#'

    result = re.sub(bold_pattern, r'<p><strong>\1</strong></p>', value)
    result = re.sub(italic_pattern, r'<p><em>\1</em></p>', result)
    result = re.sub(h2_pattern, r'<p><h2>\1</h2></p>', result)
    result = re.sub(h1_pattern, r'<p><h1>\1</h1></p>', result)

    return mark_safe(result)