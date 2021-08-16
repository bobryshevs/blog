from .base_exception import BaseAppException


class NotFound(BaseAppException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
