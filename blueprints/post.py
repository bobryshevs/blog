from exceptions.not_found import NotFound
from exceptions.bad_request import BadRequest
from flask import Blueprint, request, Response, jsonify
from structure import (
    post_presenter,
    post_service
)


post = Blueprint('post', __name__)


@post.route('/')
def get_post_page():
    page = request.args.get('page', type=int)
    page_size = request.args.get('page_size', type=int)

    try:
        posts = [
            post_presenter.to_json(post)
            for post in post_service.get_page(page, page_size)
        ]
        return jsonify(posts), 200

    except BadRequest as err:
        return str(err), 400


@post.route('/<post_id>', methods=['GET'])
def get_post_by_id(post_id: str):
    try:
        post = post_service.get_by_id(post_id)
        post_json = post_presenter.to_json(post)
        return post_json, 200

    except BadRequest as err:
        return str(err), 400

    except NotFound as err:
        return str(err), 404


@post.route('/<post_id>', methods=["DELETE"])
def delete_post_by_id(post_id: str):
    try:
        post_service.delete(post_id)
        return '', 204
    except BadRequest as err:
        return str(err), 400
    except NotFound as err:
        return str(err), 404


@post.route('/', methods=['POST'])
def create_post():
    try:
        response = Response()
        fields = request.json
        post_id = post_service.create(fields['text'], fields['author'])
        response.headers['Location'] = f'/post/{post_id}'
        return response, 201
    except BadRequest as err:
        return str(err), 400
    except NotFound as err:
        return str(err), 404


@post.route('/<post_id>', methods=['PUT'])
def update_post(post_id: str):
    try:
        fields = request.json
        upd_post = post_service.update(post_id,
                                       fields['text'],
                                       fields['author'])
        return post_presenter.to_json(upd_post), 204
    except BadRequest as err:
        return str(err), 400
    except NotFound as err:
        return str(err), 404
