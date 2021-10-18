from flask import (
    Blueprint,
    request,
)
from flasgger import swag_from

from structure import (
    create_user_handler,
    login_handler,
    refresh_handler,
    logout_handler
)
users = Blueprint("users", __name__)


@users.route("/", methods=["POST"])
@swag_from("../swagger/user/create_user.yml")
def create():
    return create_user_handler.handle(request)


@users.route("/login", methods=["POST"])
@swag_from("../swagger/user/login.yml")
def login():
    return login_handler.handle(request)


@users.route("/refresh", methods=["POST"])
@swag_from("../swagger/user/refresh.yml")
def refresh():
    return refresh_handler.handle(request)


@users.route("/logout", methods=["POST"])
@swag_from("../swagger/user/logout.yml")
def logout():
    return logout_handler.handle(request)
