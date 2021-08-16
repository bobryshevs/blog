from .base_exception import BaseAppException


class BadRequest(BaseAppException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
