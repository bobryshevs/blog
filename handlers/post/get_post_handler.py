from flask import Request

from handlers.base_handler import BaseHandler
from enums import HTTPStatus
from models import User, Post


class GetPostHandler(BaseHandler):

    def execute(self,
                request: Request,
                principle: User) -> tuple[dict, HTTPStatus]:
        post: Post = self.service.get_by_id(request.view_args)
        return self.presenter.to_json(post), HTTPStatus.OK
