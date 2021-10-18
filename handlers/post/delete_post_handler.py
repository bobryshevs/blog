from flask import Request

from handlers.base_handler import BaseHandler
from models import User


class DeletePostHandler(BaseHandler):
    def execute(self, request: Request, principle: User) -> None:
        self.service.delete(request.view_args, principle)
