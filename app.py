from flask import Flask

from config import ConfigurationTest

app = Flask(__name__)
app.config.from_object(ConfigurationTest)

@app.route('/')
def index():
    return 'Main page'


if __name__ == '__main__':
    app.run()
