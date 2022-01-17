from flask import Blueprint

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users')
def index():
    return {
        "name": "Adam Simon",
        "age": "18"
    }
