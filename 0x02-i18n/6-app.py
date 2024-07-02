#!/usr/bin/env python3
""" basic flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """ configurations class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages """
    lang = request.args.get('locale')
    if lang in app.config["LANGUAGES"]:
        return lang

    if g.user and g.user.get('locale') is not None:
        if g.user.get('locale') in app.config(["LANGUAGES"]):
            return g.user.get('locale')

    if request.headers.get('locale', None) in app.config(["LANGUAGES"]):
        return request.headers.get("locale", None)

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """ return the dict of the user """
    login = request.args.get("login_as")
    if login is not None and int(login) in users.keys():
        return users[int(login)]
    return None


@app.before_request
def before_request():
    """ use get_user to find a user if any, and set it as a global user """
    g.user = get_user()


@app.route('/')
def index():
    """ index route """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
