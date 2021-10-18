from flask import Request

from models import User
from handlers.base_handler import BaseHandler
from exceptions import Unauthorized


class LogoutHandler(BaseHandler):
    def execute(self, request: Request, principle: User) -> None:
        if principle is None:
            raise Unauthorized({"msg": "login required"})
        access: str = request.headers["Authorization"].split(" ")[1]
        self.service.logout({
            "access": access,
            "principle": principle
        })
