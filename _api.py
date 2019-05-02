"""Pytsite Hreflang Plugin API Functions
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from copy import deepcopy as _deepcopy
from pytsite import lang as _lang, router as _router, threading as _threading

_links = {}


def reset():
    """Reset links
    """
    _links[_threading.get_id()] = {}

    for lng in _lang.langs(False):
        put(lng, _router.current_url(lang=lng))


def put(lang: str, href: str):
    """Add a link
    """
    _links[_threading.get_id()][lang] = href


def get(lang: str) -> str:
    """Get a link
    """
    return _links[_threading.get_id()].get(lang)


def get_all() -> dict:
    """Get all links
    """
    return _deepcopy(_links[_threading.get_id()])


def remove(lng: str):
    """Remove a link
    """
    try:
        del _links[_threading.get_id()][lng]
    except KeyError:
        pass
