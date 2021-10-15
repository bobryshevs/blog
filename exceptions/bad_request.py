from .base_exception import BaseAppException
from enums import HTTPStatus


class BadRequest(BaseAppException):
    def __init__(self, value: dict, *args: object) -> None:
        super().__init__(*args)
        self.value = value
        self.code = HTTPStatus.BAD_REQUEST
