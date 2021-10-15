from flask import Request

from handlers.base_handler import BaseHandler
from models import User, Post
from enums import HTTPStatus
from exceptions import Forbidden


class DeletePostHandler(BaseHandler):
    def execute(self,
                request: Request,
                principle: User) -> tuple[dict, HTTPStatus]:
        print("inside delete post handler execute", flush=True)
        self.service.delete(request.view_args, principle)
        return {}, HTTPStatus.NO_CONTENT

    def _raise_forbidden(self):
        raise Forbidden(
            {
                "msg":
                "You can't delete a post that you aren't the author of"
            }
        )
