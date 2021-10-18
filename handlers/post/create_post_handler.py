from flask import Request

from handlers.base_handler import BaseHandler
from models import User, Post


class CreatePostHandler(BaseHandler):
    def execute(self, request: Request, principle: User) -> Post:
        return self.service.create(request.json, principle)
