from flask import Blueprint

provinces_blueprint = Blueprint('provinces_blueprint', __name__)


@provinces_blueprint.route('/provinces', methods=["GET"])
def get_all_health_regions():
    return {
        "provinces": [
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


@provinces_blueprint.route('/provinces/<hr_id>', methods=["GET"])
def get_health_regions_by_id(hr_id):
    return f"You're looking for the province with the id {hr_id}"
