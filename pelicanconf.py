#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Aina Frau-Pascual'
SITENAME = u'Aina Frau-Pascual'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'files']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ATOM = None
FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
TAG_FEED_ATOM = None

# Blogroll
#LINKS = (('Google scholar', 'https://scholar.google.fr/citations?user=ilC7VXwAAAAJ&hl=en&oi=sra'),
#('LinkedIn','https://www.linkedin.com/in/aina-frau-pascual-3116a936?trk=nav_responsive_tab_profile_pic'),
#('Github','https://github.com/ainafp'),
#('Research Gate','https://www.researchgate.net/profile/Aina_Frau_Pascual'),)

# Social widget
#SOCIAL = None
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL=(
#('Google Scholar', 'https://scholar.google.fr/citations?user=ilC7VXwAAAAJ&hl=en&oi=sra'),
('LinkedIn','https://www.linkedin.com/in/aina-frau-pascual-3116a936?trk=nav_responsive_tab_profile_pic'),
('Github','https://github.com/ainafp'),
#('Research Gate','https://www.researchgate.net/profile/Aina_Frau_Pascual'),
('Twitter', 'https://twitter.com/afraupascual'),
#('email', 'mailto:ainafp@gmail.com'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Template
#THEME='themes/pelican-sober'
THEME='themes/pelican-blueidea'

# Plugins
PLUGIN_PATHS=['plugins']
PLUGINS=['pelican-bibtex']

# Bibliography
PUBLICATIONS_SRC='content/files/mybiblio.bib'

