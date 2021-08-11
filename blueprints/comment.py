from flask import Blueprint, request, jsonify
from structure import comment_repository

comment = Blueprint('comment', __name__)


@comment.route('/<comment_id>', methods=['GET'])
def get_comment_by_id(comment_id: str):
    comment = comment_repository.get_by_id(comment_id)
    return comment


@comment.route('/pagination', methods=['GET'])
def get_comment_pages():
    comments = comment_repository.get_comment_pages(
        page_size=request.args.get('page_size', type=int),
        page_number=request.args.get('page_number', type=int))
    return jsonify(comments)
