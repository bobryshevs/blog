from .base_exception import BaseAppException
from enums import HTTPStatus


class Conflict(BaseAppException):
    def __init__(self, value: dict, *args: object) -> None:
        super().__init__(*args)
        self.code = HTTPStatus.CONFLICT
        self.value = value
