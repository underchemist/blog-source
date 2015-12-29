#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Yann-Sebastien'
SITENAME = 'ysebastien.xyz'
SITESUBTITLE = '"Even a turtle falls on its back without the help of a friend"'
SITEURL = 'http://ysebastien.xyz'

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
# SOCIAL = (('twitter', 'https://twitter.com/underchemist'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Customization

THEME = '../pelican-themes/clean-blog'
HEADER_COVER = 'images/header.jpg'
DISPLAY_PAGES_ON_MENU = True
COLOR_SCHEME_CSS = 'github.css'

DEFAULT_METADATA = {
    'authors': 'Yann-Sebastien',
    'status': 'draft',
}

GITHUB_URL = 'https://github.com/underchemist'
TWITTER_URL = 'https://twitter.com/underchemist'
FACEBOOK_URL = 'https://www.facebook.com/ysebastien'

DELETE_OUTPUT_DIRECTORY = False

STATIC_PATHS = ['images']
