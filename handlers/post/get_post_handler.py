from flask import Request

from handlers.base_handler import BaseHandler
from models import User, Post


class GetPostHandler(BaseHandler):

    def execute(self, request: Request, principle: User) -> Post:
        return self.service.get_by_id(request.view_args)
