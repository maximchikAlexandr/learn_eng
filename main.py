"""Create flask-application"""

from flask import Flask, redirect, render_template, url_for
from flask_migrate import Migrate

from config import ConfigurationTest
from dct.main import dct_bp
from extensions import db
from user.main import login_manager, user_bp

app = Flask(__name__)
app.config.from_object(ConfigurationTest)
db.init_app(app)  # allow to use flask_sqlalchemy with Blueptint
migrate = Migrate(app, db)
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(dct_bp, url_prefix="/dct")
login_manager.init_app(app=app)


@app.route("/")
def index():
    return redirect(url_for("dct.index"))


@app.errorhandler(404)
def page_not_found(_) -> str:
    return render_template("user/page404.html", title="Page is not found")
