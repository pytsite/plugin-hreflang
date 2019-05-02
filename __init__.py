"""Pytsite Hreflang Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from ._api import put, get, get_all, remove, reset


def plugin_load_wsgi():
    from pytsite import events, metatag, lang, router

    if lang.langs(False):
        def metatag_dump_all_eh():
            for lng, href in get_all().items():
                if lng != lang.get_current():
                    metatag.t_set('link', rel='alternate', href=href, hreflang=lng)

        router.on_dispatch(reset)
        events.listen('pytsite.metatag@dump_all', metatag_dump_all_eh)
