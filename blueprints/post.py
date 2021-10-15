from flask import (
    Blueprint,
    request,
)
from flasgger import swag_from

from structure import (
    create_post_handler,
    get_post_handler,
    delete_post_handler,
    update_post_handler,
    get_post_page_handler
)
post = Blueprint("post", __name__)


@post.route("/")
@swag_from("../swagger/post/get_post_page.yml")
def get_post_page():
    return get_post_page_handler.handle(request)


@post.route("/<id>", methods=["GET"])
@swag_from("../swagger/post/get_post_by_id.yml")
def get_post_by_id(id: str):
    return get_post_handler.handle(request)


@post.route("/<id>", methods=["DELETE"])
@swag_from("../swagger/post/delete_post_by_id.yml")
def delete_post_by_id(id: str):
    print("inside blueprint", flush=True)
    return delete_post_handler.handle(request)


@post.route("/", methods=["POST"])
@swag_from("../swagger/post/create_post.yml")
def create_post():
    return create_post_handler.handle(request)


@post.route("/<id>", methods=["PUT"])
@swag_from("../swagger/post/update_post.yml")
def update_post(id: str):
    return update_post_handler.handle(request)
