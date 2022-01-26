from flask import Flask
from routes_pkg.health_regions import *
from routes_pkg.fsa import *
from routes_pkg.provinces import *

app = Flask(__name__)
app.register_blueprint(health_regions_blueprint)
app.register_blueprint(provinces_blueprint)
# app.register_blueprint(fsa_blueprint)


@app.route('/')
def hello_world():
    return "Default api endpoint!!! TEST"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
