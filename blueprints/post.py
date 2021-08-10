from flask.wrappers import Request
from flask import Blueprint, request, Response
from structure import post_repository


post = Blueprint('post', __name__)


@post.route('/<post_id>', methods=['GET'])
def get_post_by_id(post_id: str):
    post = post_repository.get_post_by_id(post_id)
    return post


@post.route('/<post_id>', methods=["DELETE"])
def delete_post_by_id(post_id: str):
    return post_repository.delete_post_by_id(post_id)


@post.route('/', methods=['POST'])
def create_post():
    response = Response()
    fields = request.json
    post_id = post_repository.create_new_post(fields['text'], fields['author'])
    response.headers['Location'] = f'/post/{post_id}'
    response.status_code = 201
    return response
    
@post.route('/<post_id>', methods=['PUT'])
def update_post(post_id: str):
    fields = request.json
    post_repository.update_post_by_id(post_id=post_id,
                                      text=fields['text'],
                                      author=fields['author'])

    # ToDo: Узнать про дату создания, т.к. по REST необходимо обновлять все поля

    return '', 204
