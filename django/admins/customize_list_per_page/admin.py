""" By default, Django admin ``list_per_page = 100``,
    And this value can only be set in a admin class.

    The following implementation allows to set **user-preferred**
    ``list_per_page`` at admin ``change_list_view.html``.
"""

from django.contrib import admin
from django.core.checks import messages
from django.utils.translation import ugettext as _, ugettext_lazy


class CustomizedListPerPageAdmin(admin.ModelAdmin):
    """ Implemented by set_cookies of customize_list_per_page
    """
    # Default
    default_list_per_page = 100

    def get_list_per_page(self, request):
        if request.POST.get('customize_list_per_page'):
            try:
                list_per_page = int(request.POST.get('customize_list_per_page'))
            except:
                self.message_user(request, _('输入有误'), level=messages.ERROR)
                return CustomizedListPerPageAdmin.default_list_per_page
            if list_per_page < 1 or list_per_page > 5000:
                self.message_user(request, _('太小 / 太大'), level=messages.WARNING)
                return CustomizedListPerPageAdmin.default_list_per_page
            return list_per_page
        elif request.COOKIES.get('customize_list_per_page'):
            return int(request.COOKIES.get('customize_list_per_page'))
        return CustomizedListPerPageAdmin.default_list_per_page

    def set_list_per_page(self, request, response, max_age=30 * 24 * 3600):
        if not request.POST.get('customize_list_per_page'):
            return
        response.set_cookie('customize_list_per_page', self.list_per_page, max_age)

    def changelist_view(self, request, extra_context=None):
        self.list_per_page = self.get_list_per_page(request)
        response = super(CustomizedListPerPageAdmin, self).changelist_view(
            request,
            extra_context,
        )
        self.set_list_per_page(request, response)
        return response

