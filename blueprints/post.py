from flask import (
    Blueprint,
    request,
    jsonify,
)
from flasgger import swag_from

from structure import (
    post_presenter,
    post_service
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
    try:
        post = post_service.get_by_id({"id": id})
    except NotFound as err:
        return jsonify(err.value), 404
    except BadRequest as err:
        return jsonify(err.value), 400

    return post_presenter.to_json(post), 200


@post.route("/<id>", methods=["DELETE"])
@swag_from("../swagger/post/delete_post_by_id.yml")
def delete_post_by_id(id: str):
    try:
        post_service.delete({"id": id})
    except NotFound as err:
        return jsonify(err.value), 404
    except BadRequest as err:
        return jsonify(err.value), 400

    return "", 204


@post.route("/", methods=["POST"])
@swag_from("../swagger/post/create_post.yml")
def create_post():
    try:
        post = post_service.create(request.json)
    except BadRequest as err:
        return jsonify(err.value), 400

    return post_presenter.to_json(post), 200


@post.route("/<id>", methods=["PUT"])
@swag_from("../swagger/post/update_post.yml")
def update_post(id: str):
    fields = request.json | {"id": id}
    try:
        upd_post = post_service.update(fields)
    except BadRequest as err:
        return jsonify(err.value), 400
    except NotFound as err:
        return jsonify(err.value), 404
    return post_presenter.to_json(upd_post), 200
