from flask import (
    Blueprint,
    request,
    jsonify,
)
from flasgger import swag_from

from structure import (
    post_presenter,
    post_service,
    create_post_handler,
    get_post_handler,
    delete_post_handler,
    update_post_handler
)
from exceptions import (
    NotFound,
    BadRequest
)

post = Blueprint("post", __name__)


@post.route("/")
@swag_from("../swagger/post/get_post_page.yml")
def get_post_page():
    page = request.args.get("page", default=1, type=int)
    page_size = request.args.get("page_size", default=10, type=int)
    try:
        page = post_service.get_page(
            {
                "page": page,
                "page_size": page_size
            }
        )
    except BadRequest as err:
        return jsonify(err.value), 400

    page["items"] = [post_presenter.to_json(post) for post in page["items"]]
    return jsonify(page), 200


@post.route("/<id>", methods=["GET"])
@swag_from("../swagger/post/get_post_by_id.yml")
def get_post_by_id(id: str):
    return get_post_handler.handle(request)


@post.route("/<id>", methods=["DELETE"])
@swag_from("../swagger/post/delete_post_by_id.yml")
def delete_post_by_id(id: str):
    return delete_post_handler.handle(request)


@post.route("/", methods=["POST"])
@swag_from("../swagger/post/create_post.yml")
def create_post():
    return create_post_handler.handle(request)


@post.route("/<id>", methods=["PUT"])
@swag_from("../swagger/post/update_post.yml")
def update_post(id: str):
    return update_post_handler.handle(request)
