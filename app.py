from flask import Flask, redirect, url_for

from config import ConfigurationTest
from extensions import db
from user.main import user_bp

app = Flask(__name__)
app.config.from_object(ConfigurationTest)
db.init_app(app) # allow to use flask_sqlalchemy with Blueptint
app.register_blueprint(user_bp, url_prefix='/user')


@app.route('/')
def index():
    return '''
    <p><a href="/user/register"> Registration </a>
    <p><a href="/user/login"> Login </a>
    '''

if __name__ == '__main__':
    app.run()
