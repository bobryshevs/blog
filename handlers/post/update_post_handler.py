from flask import Request

from handlers.base_handler import BaseHandler
from models import User, Post
from enums import HTTPStatus
from exceptions import Forbidden


class UpdatePostHandler(BaseHandler):

    def execute(self,
                request: Request,
                principle: User) -> tuple[dict, HTTPStatus]:
        args = request.json | request.view_args
        post: Post = self.service.update(args, principle)
        return self.presenter.to_json(post), HTTPStatus.OK
