from translators import post_tranlator
from services.comment_service import CommentService
from flask import (
    Blueprint,
    request,
    jsonify
)
from structure import (
    comment_service,
    comment_presenter
)
from exceptions import (
    NotFound,
    BadRequest
)

comment = Blueprint('comment', __name__)


@comment.route('/', methods=['GET'])
def get_comment_page():
    post_id = request.args.get('post_id', type=str),
    page = request.args.get('page', type=int)
    page_size = request.args.get('page_size', type=int),

    try:
        page = [
            comment_presenter.to_json(comment)
            for comment in comment_service.get_page(post_id, page, page_size)
        ]
        return jsonify(page), 200

    except BadRequest as err:
        return str(err), 400

    except NotFound as err:
        return str(err), 404  # If post doesn't exist


# @comment.route('/<comment_id>', methods=['GET'])
# def get_comment_by_id(comment_id: str):
    # try:
    #     comment = comment_service.get
    # return comment
