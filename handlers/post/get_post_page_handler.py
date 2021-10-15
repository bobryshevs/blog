from flask import Request

from handlers.base_handler import BaseHandler
from models import User
from enums import HTTPStatus


class GetPostPageHanlder(BaseHandler):
    def execute(self,
                request: Request,
                principle: User) -> tuple[dict, HTTPStatus]:
        page: list[dict] = self.service.get_page(
            {
                "page": request.args.get("page", 1, int),  # arg, default, type
                "page_size": request.args.get("page_size", 10, int)
            }
        )
        page["items"] = [
            self.presenter.to_json(post)
            for post in page["items"]
        ]
        return page, HTTPStatus.OK
