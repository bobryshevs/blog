from flask import (
    Blueprint,
    request,
    jsonify
)
from flasgger import swag_from

from structure import (
    user_service,
    user_presenter,
    token_pair_presenter
)
from exceptions import (
    Conflict,
    BadRequest
)
users = Blueprint("users", __name__)


@users.route("/", methods=["POST"])
@swag_from("../swagger/user/create_user.yml")
def create():
    try:
        user = user_service.create(request.json)
    except BadRequest as err:
        return jsonify(err.value), err.code
    except Conflict as err:
        return jsonify(err.value), err.code
    return user_presenter.to_json(user), 200


@users.route("/login", methods=["POST"])
@swag_from("../swagger/user/login.yml")
def login():
    try:
        tockens = user_service.login(request.json)
    except BadRequest as err:
        return jsonify(err.value), err.code
    return jsonify(token_pair_presenter.to_json(tockens)), 200
