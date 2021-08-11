from flask import Blueprint, request, Response, jsonify
from structure import post_repository, post_translator
from structure import post_presenter


post = Blueprint('post', __name__)

@post.route('/pagination')
def get_post_pages():
    page_number = request.args.get('page_number', type=int)
    page_size = request.args.get('page_size', type=int)
    posts = post_repository.get_pages(page_number, page_size)
    return jsonify(posts)


@post.route('/', methods=['GET'])
def get_multiple_posts_by_IDs():
    IDs = request.args.values()
    posts = [
        post_repository.get_by_id(post_id) 
        for post_id in IDs
    ]
    return jsonify(posts)



@post.route('/<post_id>', methods=['GET'])
def get_post_by_id(post_id: str):
    post = post_repository.get_by_id(post_id)
    if post is None:
        return '', 404
    post_obj = post_translator.from_mongo(post)
    post_json = post_presenter.to_json(post_obj)
    return post, 200


@post.route('/<post_id>', methods=["DELETE"])
def delete_post_by_id(post_id: str):
    if post_repository.delete_by_id(post_id):
        return '', 204
    else:
        return '', 404


@post.route('/', methods=['POST'])
def create_post():
    response = Response()
    fields = request.json
    post_id = post_repository.create(fields['text'], fields['author'])
    response.headers['Location'] = f'/post/{post_id}'
    response.status_code = 201
    return response


@post.route('/<post_id>', methods=['PUT'])
def update_post(post_id: str):
    fields = request.json
    post_repository.update(post_id=post_id,
                            text=fields['text'],
                            author=fields['author'])
    return '', 204
