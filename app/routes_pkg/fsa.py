from flask import Blueprint

fsa_blueprint = Blueprint('fsa_blueprint', __name__)


@fsa_blueprint.route('/fsa')
def all_fsas():
    return {
        "fsas": [
            "A0A",
            "A0B",
            "A1S"
        ]
    }
