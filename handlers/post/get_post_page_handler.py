from flask import Request

from handlers.base_handler import BaseHandler
from models import User, Page


class GetPostPageHandler(BaseHandler):
    def execute(self, request: Request, principle: User) -> Page:
        page: Page = self.service.get_page(
            {
                "page": request.args.get("page", 1, int),  # arg, default, type
                "page_size": request.args.get("page_size", 10, int)
            }
        )
        return page
