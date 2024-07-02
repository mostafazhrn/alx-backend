#!/usr/bin/env python3
""" THis script starts a Flask web application """
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Union
import pytz
from pytz import exceptions


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ this shall reptesent the config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request(login_as: int = None):
    """ this function shall set the user locale """
    user: dict = get_user()
    print(user)
    g.user = user


def get_user() -> Union[dict, None]:
    """ this function shall return a user dict or None """
    login_usr = request.args.get('login_as', None)
    if login_usr is None:
        return None
    user: dict = {}
    user[login_usr] = users.get(int(login_usr))
    return user[login_usr]


@babel.localeselector
def get_locale():
    """ this function shall return the best match of supported languages """
    local = request.args.get('locale', None)
    if local and local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """ this function shall return the user's timezone """
    try:
        if request.args.get('timezone'):
            tm_zone = request.args.get('timezone')
            zone = pytz.timezone(tm_zone)
        elif g.user and g.user.get('timezone'):
            tm_zone = g.user.get('timezone')
            zone = pytz.timezone(tm_zone)
        else:
            tm_zone = app.config['BABEL_DEFAULT_TIMEZONE']
            zone = pytz.timezone(tm_zone)
    except exceptions.UnknownTimeZoneError:
        tm_zone = 'UTC'
    return tm_zone


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ This function returns a string """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
