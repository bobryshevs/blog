from flask import Request

from handlers.base_handler import BaseHandler
from models import User, Post
from enums import HTTPStatus
from exceptions import Forbidden


class UpdatePostHandler(BaseHandler):

    def execute(self,
                request: Request,
                principle: User) -> tuple[dict, HTTPStatus]:
        self.principle_check_none(principle)
        post: Post = self.service.get_by_id(request.view_args)
        if post.author_id != principle.id:
            self._raise_forbidden()
        args = request.json | {"author_id": post.author_id} | request.view_args
        post = self.service.update(args)
        return self.presenter.to_json(post), HTTPStatus.OK

    def _raise_forbidden(self):
        raise Forbidden(
            {
                "msg":
                "You can't update a post that you aren't the author of"
            }
        )
