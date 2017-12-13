"""Pytsite Hreflang Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

if _plugman.is_installed(__name__):
    # Public API
    from ._api import add, get, get_all, reset


def plugin_load():
    from pytsite import events, metatag, lang, router

    def metatag_dump_all_eh():
        for lng, href in get_all().items():
            if lng != lang.get_current():
                metatag.t_set('link', rel='alternate', href=href, hreflang=lng)

    router.on_dispatch(reset)
    events.listen('pytsite.metatag@dump_all', metatag_dump_all_eh)
