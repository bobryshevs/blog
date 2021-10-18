from flask import Request

from models import User, TokenPair
from handlers.base_handler import BaseHandler


class LoginHandler(BaseHandler):
    def execute(self, request: Request, principle: User) -> TokenPair:
        return self.service.login(request.json)
