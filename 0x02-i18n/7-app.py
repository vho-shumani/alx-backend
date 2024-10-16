from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Define config parameter"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    """get user"""
    login_as = request.args.get('login_as')
    if login_as:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    """get user"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """get locale"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """get timezone"""
    try:
        timezone = request.args.get('timezone')
        if timezone:
            return pytz.timezone(timezone).zone
        if g.user and g.user['timezone']:
            return pytz.timezone(g.user['timezone']).zone

    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """home page"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
