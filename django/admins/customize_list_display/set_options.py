# coding: utf-8

"""Admin Template Tags Functions
"""

from django.contrib.admin.utils import label_for_field
from django.template import Library
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _, ugettext_lazy

from .models import MyModel
from .admin import CustomizedListDisplayAdmin

register = Library()


@register.simple_tag
def set_options(list_display):
    labels = {k: label_for_field(k, MyModel, CustomizedListDisplayAdmin)
              for k, _ in list_display.items()}
    return format_html_join(
        '\n', mark_safe('<option value="{}"><strong>{}»</strong> {}</option>'),
        ((k, _('+ 显示') if v == 0 else _('- 隐藏'),
          labels.get(k) if labels.get(k) else k) for k, v in list_display.items())
    )
