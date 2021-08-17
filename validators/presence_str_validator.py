from collections import namedtuple
from .validator import Validator


class PresenceStrValidator(Validator):
    def __init__(self, key: str) -> None:
        super().__init__(key)

    def validate(self, args: dict) -> bool:

        if not isinstance(args, dict):
            return self.INVALID_TYPE_CODE

        if self.key not in args:
            return self.INVALID_VALUE_CODE

        if not isinstance(args.get(self.key), str):
            return self.INVALID_TYPE_CODE

        if not self.key:
            return self.INVALID_VALUE_CODE

        return self.VALID

        # Вернуть в сервис валидатора код ошибки и там выбросить
        # нужный exception, чтобы не терять производительность
        # и соотносить разные варианты ошибок с соответствующими
        # исключениями
