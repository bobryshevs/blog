from flask import Request

from models import User
from handlers.base_handler import BaseHandler


class CreateUserHandler(BaseHandler):
    def execute(self, request: Request, principle: User) -> User:
        return self.service.create(request.json)
