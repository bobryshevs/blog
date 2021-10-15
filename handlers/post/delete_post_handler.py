from flask import Request

from handlers.base_handler import BaseHandler
from models import User, Post
from enums import HTTPStatus
from exceptions import Forbidden


class DeletePostHandler(BaseHandler):
    def execute(self,
                request: Request,
                principle: User) -> tuple[dict, HTTPStatus]:

        self.principle_check_none(principle)
        post: Post = self.service.get_by_id(request.view_args)
        if principle.id != post.author_id:
            self._raise_forbidden()

        self.service.delete({"id": post.id})
        return {}, HTTPStatus.NO_CONTENT

    def _raise_forbidden(self):
        raise Forbidden(
            {
                "msg":
                "You can't delete a post that you aren't the author of"
            }
        )
