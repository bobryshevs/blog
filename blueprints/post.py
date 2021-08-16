from bson import is_valid
from bson.objectid import ObjectId, InvalidId
from flask import Blueprint, request, Response, jsonify
from structure import (
    post_repository,
    post_presenter,
    post_validator,
    post_service
)


post = Blueprint('post', __name__)


@post.route('/pagination')
def get_post_page():
    page = request.args.get('page', type=int)
    page_size = request.args.get('page_size', type=int)

    if not isinstance(page, int) \
            or not isinstance(page_size, int) \
            or page < 1 \
            or page_size < 1:
        return '', 400

    posts = [
        post_presenter.to_json(post)
        for post in post_service.get_page(page, page_size)
    ]
    return jsonify(posts), 200


@post.route('/<post_id>', methods=['GET'])
def get_post_by_id(post_id: str):
    if not ObjectId.is_valid(post_id):
        return '', 400

    post = post_service.get_by_id(ObjectId(post_id))

    if post is None:
        return '', 404

    post_json = post_presenter.to_json(post)
    return post_json, 200


@post.route('/', methods=['GET'])
def get_multiple_posts_by_IDs():
    IDs = list(request.args.values())

    for index, post_id in enumerate(IDs):
        if ObjectId.is_valid(post_id):
            IDs[index] = ObjectId(post_id)
        else:
            return '', 400

    posts = [
        post_presenter.to_json(
            post_repository.get_by_id(post_id)
        )
        for post_id in IDs
    ]
    return jsonify(posts), 200


@post.route('/<post_id>', methods=["DELETE"])
def delete_post_by_id(post_id: str):
    if not ObjectId.is_valid(post_id):
        return '', 400
    if post_service.delete(ObjectId(post_id)):
        return '', 204
    else:
        return '', 404


@post.route('/', methods=['POST'])
def create_post():
    response = Response()
    fields = request.json

    if not isinstance(fields['text'], str) \
            or not isinstance(fields['author'], str):
        return '', 400

    post_id = post_service.create(fields['text'], fields['author'])
    response.headers['Location'] = f'/post/{post_id}'
    return response, 201


@post.route('/<post_id>', methods=['PUT'])
def update_post(post_id: str):
    fields = request.json

    if not isinstance(post_id, str) \
            or not isinstance(fields['text'], str) \
            or not isinstance(fields['author'], str) \
            or not ObjectId.is_valid(post_id):
        return '', 400

    upd_post = post_service.update(ObjectId(post_id),
                                   fields['text'],
                                   fields['author'])

    if upd_post is None:
        return '', 400

    return post_presenter.to_json(upd_post), 200
