from flask import Request

from handlers.base_handler import BaseHandler
from enums import HTTPStatus
from models import User, Post


class CreatePostHandler(BaseHandler):
    def execute(self,
                request: Request,
                principle: User) -> tuple[dict, HTTPStatus]:
        args: dict = request.json | {"author_id": principle.id}
        post: Post = self.service.create(args)
        return self.presenter.to_json(post), HTTPStatus.CREATED
