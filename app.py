from flask import Flask
from routes_pkg.health_region import *
from routes_pkg.fsa import *

app = Flask(__name__)
app.register_blueprint(users_blueprint)
app.register_blueprint(fsa_blueprint)


@app.route('/')
def hello_world():
    return "Default api endpoint"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
