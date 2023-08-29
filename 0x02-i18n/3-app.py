#!/usr/bin/env python3
'''
    Use Babel to get user locale.
'''

from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    '''
        Babel configuration.
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
