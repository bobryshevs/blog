from flask import Request

from handlers.base_handler import BaseHandler
from models import User, Post


class UpdatePostHandler(BaseHandler):

    def execute(self, request: Request, principle: User) -> Post:
        args = request.json | request.view_args
        return self.service.update(args, principle)
