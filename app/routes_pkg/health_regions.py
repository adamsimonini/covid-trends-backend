from flask import Blueprint

health_regions_blueprint = Blueprint('health_regions_blueprint', __name__)


@health_regions_blueprint.route('/health_regions', methods=["GET"])
def get_all_health_regions():
    return {
        "health_regions": [
            {
                "hr_uid": "599",
                "english_name": "Interior",
                "french_name": "Interior"
            },
            {
                "hr_uid": "1110",
                "english_name": "Toronto Health",
                "french_name": "Toronto Health"
            }
        ]
    }


@health_regions_blueprint.route('/health_regions/<hr_id>', methods=["GET"])
def get_health_regions_by_id(hr_id):
    return f"You're looking for the health region with the id {hr_id}"
