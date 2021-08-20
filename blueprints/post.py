import re
from exceptions import (
    NotFound,
    BadRequest
)
from flask import (
    Blueprint,
    request,
    jsonify,
    make_response
)
import exceptions
from structure import (
    post_presenter,
    post_service
)
import json

post = Blueprint('post', __name__)


@post.route('/')
def get_post_page():
    page = request.args.get('page', type=int)
    page_size = request.args.get('page_size', type=int)
    try:
        posts = [
            post_presenter.to_json(post)
            for post in post_service.get_page({
                'page': page,
                'page_size': page_size
            })
        ]
        return jsonify(posts), 200

    except BadRequest as err:
        return str(err), 400


@post.route('/<post_id>', methods=['GET'])
def get_post_by_id(post_id: str):
    try:
        post = post_service.get_by_id({'post_id': post_id})
    except NotFound as err:
        return str(err), 404
    except BadRequest as err:
        return str(err), 404  # Must be 400

    return post_presenter.to_json(post), 200


@post.route('/<post_id>', methods=["DELETE"])
def delete_post_by_id(post_id: str):
    try:
        post_service.delete({'post_id': post_id})
        return '', 204
    except NotFound as err:
        return str(err), 404
    except BadRequest as err:
        return str(err), 404  # Must be 400


@post.route('/', methods=['POST'])
def create_post():
    fields = request.json
    try:
        post = post_service.create(fields)
    except BadRequest as err:
        return str(err), 400
    response = make_response(post_presenter.to_json(post))
    response.headers['Location'] = f'/post/{post.id}'
    response.status_code = 201
    return response


@post.route('/<post_id>', methods=['PUT'])
def update_post(post_id: str):
    try:
        fields = request.json | {'post_id': post_id}
        upd_post = post_service.update(fields)
        return post_presenter.to_json(upd_post), 200
    except BadRequest as err:
        return str(err), 400
    except NotFound as err:
        return str(err), 404
