from flask import Request

from models import User, TokenPair
from enums import HTTPStatus
from handlers.base_handler import BaseHandler


class RefreshHandler(BaseHandler):
    def execute(self,
                request: Request,
                principle: User) -> tuple[dict, HTTPStatus]:
        tokens: TokenPair = self.service.refresh(request.json)
        return self.presenter.to_json(tokens), HTTPStatus.OK
