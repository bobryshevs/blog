from .base_exception import BaseAppException


class NotFound(BaseAppException):
    def __init__(self, value: dict = None, *args: object) -> None:
        super().__init__(*args)
        self.set_value(value)
        self.code = 404

    def set_value(self, value) -> None:
        if value:
            self.value = value
        else:
            self.value = {"msg": "NotFound"}
