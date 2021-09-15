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


post = Blueprint('post', __name__)


@post.route('/')
def get_post_page():
    page = request.args.get('page', default=1, type=int)
    page_size = request.args.get('page_size', defalut=10, type=int)
    try:
        post_obj_list = post_service.get_page(
            {
                'page': page,
                'page_size': page_size
            }
        )
    except BadRequest as err:
        return str(err), 400

    posts = [post_presenter.to_json(post) for post in post_obj_list]
    return jsonify(posts), 200


@post.route('/<id>', methods=['GET'])
@swag_from('./yml_views/get_post_by_id.yml')
def get_post_by_id(id: str):
    try:
        post = post_service.get_by_id({'id': id})
    except NotFound as err:
        return str(err), 404
    except BadRequest as err:
        return str(err), 400

    return post_presenter.to_json(post), 200


@post.route('/<id>', methods=["DELETE"])
def delete_post_by_id(id: str):
    try:
        post_service.delete({'id': id})
    except NotFound as err:
        return str(err), 404
    except BadRequest as err:
        return str(err), 400

    return '', 204


@post.route('/', methods=['POST'])
def create_post():
    try:
        post = post_service.create(request.json)
    except BadRequest as err:
        return str(err), 400

    return post_presenter.to_json(post), 200


@post.route('/<id>', methods=['PUT'])
def update_post(id: str):
    fields = request.json | {'id': id}
    try:
        upd_post = post_service.update(fields)
    except BadRequest as err:
        return str(err), 400
    except NotFound as err:
        return str(err), 404

    return post_presenter.to_json(upd_post), 200
