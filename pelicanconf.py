#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"Jacob's Rape Victims Collective"
SITENAME = u'Jacob Appelbaum'
SITEURL = ''

PATH = 'content'

#################
# Theme stuff
#################
THEME = 'plugins/pelican-free-agent'
THEME_STATIC_DIR = 'theme'

BOOTSTRAP_FILE = 'bootstrap.min.css'
CSS_FILE = 'freeagent.css'
FONTS = 'fonts'
SCRIPTS = [
	'jquery-1.11.0.js',
	'bootstrap.min.js',
	'jquery.easing.min.js',
	'classie.js',
        'cbpAnimatedHeader.js',
	'jqBootstrapValidation.js',
        #'openpgp.js',
        #'openpgp.worker.js',
	#'contact_me.js',
        'nacl_factory.js',
	'contact_nacl.js',
	'freeagent.js'
]
DIRECT_TEMPLATES = ['index']
NAVLINKS = (
	#('#page-top', 'Home'),
	('#about', 'About'),
	('#stories','Stories'),
	('#victims', 'Victims'),
        ('#faq', 'FAQ'),
	('#contact', 'Contact')
)
SITETITLE = u'Jacob Appelbaum'
#SITESUBTITLE = u"""accounts from my sexual abuse victims"""
SITESUBTITLE = u''
####################
# end theme stuff
####################

TIMEZONE = 'Etc/UTC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_RSS = u'feed.rss.xml'
FEED_ALL_RSS = u'all.rss.xml'
FEED_ATOM = u'feed.atom.xml'
FEED_ALL_ATOM = u'all.atom.xml'
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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
