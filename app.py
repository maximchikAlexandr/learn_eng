from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from config import ConfigurationTest
from user.main import user_bp

app = Flask(__name__)
app.config.from_object(ConfigurationTest)
app.register_blueprint(user_bp, url_prefix='/user')

db = SQLAlchemy(app)

@app.route('/')
def index():
    return redirect(url_for('user.login'))


if __name__ == '__main__':
    app.run()
