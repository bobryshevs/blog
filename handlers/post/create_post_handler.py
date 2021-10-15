from flask import Request

from handlers.base_handler import BaseHandler
from enums import HTTPStatus
from models import User, Post


class CreatePostHandler(BaseHandler):
    def execute(self,
                request: Request,
                principle: User) -> tuple[dict, HTTPStatus]:
        post: Post = self.service.create(request.json, principle)
        return self.presenter.to_json(post), HTTPStatus.CREATED
