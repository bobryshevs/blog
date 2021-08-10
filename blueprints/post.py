from repositories.posts_repository import PostRepository
from flask import Blueprint
from structure import post_repository


post = Blueprint('post', __name__)


@post.route('/<post_id>', methods=['GET'])
def get_post_by_id(post_id: str):
    post = post_repository.get_post_by_id(post_id)
    return post


@post.route('/<post_id>', methods=["DELETE"])
def delete_post_by_id(post_id: str):
    return post_repository.delete_post_by_id(post_id)

