from flask import Flask

from config import ConfigurationTest
from user.main import user_bp

app = Flask(__name__)
app.config.from_object(ConfigurationTest)
app.register_blueprint(user_bp, url_prefix='/user')

@app.route('/')
def index():
    return 'Main page'


if __name__ == '__main__':
    app.run()
