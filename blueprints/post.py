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
from structure import (
    post_presenter,
    post_service
)
import json

post = Blueprint('post', __name__)


@post.route('/')
def get_post_page():
    try:
        posts = [
            post_presenter.to_json(post)
            for post in post_service.get_page(request.args)
        ]
        return jsonify(posts), 200

    except BadRequest as err:
        return str(err), 400


@post.route('/<post_id>', methods=['GET'])
def get_post_by_id(post_id: str):
    try:
        post = post_service.get_by_id(post_id)
    except NotFound as err:
        return str(err), 404

    return post_presenter.to_json(post), 200


@post.route('/<post_id>', methods=["DELETE"])
def delete_post_by_id(post_id: str):
    try:
        post_service.delete(post_id)
        return '', 204
    except NotFound as err:
        return str(err), 404


@post.route('/', methods=['POST'])
def create_post():
    fields = request.json
    try:
        post = post_service.create(fields['text'], fields['author'])
    except BadRequest as err:
        return str(err), 400
    response = make_response(post_presenter.to_json(post))
    response.headers['Location'] = f'/post/{post.id}'
    response.status_code = 201
    return response


@post.route('/<post_id>', methods=['PUT'])
def update_post(post_id: str):
    fields = request.json
    try:
        upd_post = post_service.update(post_id,
                                       fields['text'],
                                       fields['author'])
        return post_presenter.to_json(upd_post), 200
    except BadRequest as err:
        return str(err), 400
    except NotFound as err:
        return str(err), 404
