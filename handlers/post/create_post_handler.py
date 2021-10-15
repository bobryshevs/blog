from flask import Request

from handlers.base_handler import BaseHandler
from enums import HTTPStatus
from models import User, Post
from exceptions import Unauthorized


class CreatePostHandler(BaseHandler):
    def execute(self,
                request: Request,
                principle: User) -> tuple[dict, HTTPStatus]:
        self.principle_check_none(principle)
        args: dict = request.json | {"author_id": principle.id}
        post: Post = self.service.create(args)
        return self.presenter.to_json(post), HTTPStatus.CREATED
