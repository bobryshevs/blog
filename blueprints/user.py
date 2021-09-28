from flask import (
    Blueprint,
    request,
    jsonify
)
from structure import (
    user_service,
    user_presenter
)
from exceptions import (
    NotFound,
    BadRequest
)
from flasgger import swag_from

users = Blueprint("users", __name__)


@users.route("/", methods=["POST"])
@swag_from("../swagger/user/create_user.yml")
def create():
    try:
        user = user_service.create(request.json)
    except BadRequest as err:
        return jsonify(err.value), 400
    return user_presenter.to_json(user), 200
