""" By default, Django admin ``list_display`` can only
    be set in a admin class.

    The following implementation allows to set **user-preferred**
    ``list_display`` at admin ``change_list_view.html``.
"""

from collections import OrderedDict

from django.contrib import admin
from django.core.cache import cache
_ = None


class CustomizedListDisplayAdmin(admin.ModelAdmin):
    """ Implemented by set_cache of customize_list_display
    """
    list_display = ()

    def gen_user_key(self, username, prefix='list_display.'):
        return prefix + username

    def cache_list_display(self, userkey, list_display_dict, timeout=None):
        cache.set(userkey, list_display_dict, timeout=timeout)

    def handle_list_display(self, request):
        user_key = self.gen_user_key(str(request.user))
        posted_list_display_item = request.POST.get('list_display_item')
        if not cache.get(user_key) or posted_list_display_item == 'all':
            list_display = CustomizedListDisplayAdmin.list_display
            self.cache_list_display(
                user_key,
                OrderedDict.fromkeys(list_display, 1)
            )
            return list_display

        cached_list_display = cache.get(user_key)
        if posted_list_display_item:
            try:
                cached_list_display[posted_list_display_item] ^= 1
            except:
                return self.list_display
            self.cache_list_display(user_key, cached_list_display)

        return [k for k, v in cache.get(user_key).items()
                if v != 0]

    def changelist_view(self, request, extra_context=None):
        self.list_display = self.handle_list_display(request)
        extra_context = dict(
            user_list_display=cache.get(self.gen_user_key(str(request.user)))
        )
        response = super(CustomizedListDisplayAdmin, self).changelist_view(
            request,
            extra_context,
        )
        return response

