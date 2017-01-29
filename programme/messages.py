#!/usr/bin/python3.5
# -*-coding:Utf-8 -*
"""A file with arparse and i18n"""
import argparse, gettext
from command_line import args
gettext.install('messages','./i18n')

### i18n ###
loc = './i18n'
francais = gettext.translation('messages',loc,languages=['fr'])
english = gettext.translation('messages',loc,languages=['en'])
latina = gettext.translation('messages',loc,languages=['la_LA'])

if args.langue == 'francais':
    francais.install()
elif args.langue == 'latina':
    latina.install()
else:
    english.install()
    

### Messages ###
theochrone_messages = {} # a dict with all the messages used in theochrone.py
adjutoria_messages = { # functions # classes
    _('francais'),
    _('english'),
    _('latina'),
    } # a dict with all the messages used in adjutoria.py : first functions, second classes

