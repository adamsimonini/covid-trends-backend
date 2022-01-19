from flask import Blueprint

users_blueprint = Blueprint('health_region_blueprint', __name__)


@users_blueprint.route('/health_regions')
def index():
    return {
        "hr_uid": "599",
        "english_name": "Interior",
        "french_name": "Interior"
    }
