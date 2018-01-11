#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Yann-Sebastien'
SITENAME = 'ysebastien.me'
SITESUBTITLE = '"Even a turtle falls on its back without the help of a friend"'
SITEURL = 'http://ysebastien.me'

PATH = 'content'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/underchemist'),
          ('github', 'https://github.com/underchemist'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Customization

THEME = '../pelican-themes/clean-blog'
HEADER_COVER = 'images/header.jpg'
DISPLAY_PAGES_ON_MENU = True
COLOR_SCHEME_CSS = 'github.css'
FAVICON = 'favicon.ico'
# MENUITEMS = []

DEFAULT_METADATA = {
    'authors': 'Yann-Sebastien',
    'status': 'draft',
}

DELETE_OUTPUT_DIRECTORY = False

STATIC_PATHS = ['images', 'cv', 'extra/favicon.ico', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'}
    }
