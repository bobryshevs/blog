from flask import Request

from enums import HTTPStatus
from models import User
from handlers.base_handler import BaseHandler


class CreateUserHandler(BaseHandler):
    def execute(self,
                request: Request,
                principle: User) -> tuple[dict, HTTPStatus]:
        user: User = self.service.create(request.json)
        return self.presenter.to_json(user), HTTPStatus.CREATED
