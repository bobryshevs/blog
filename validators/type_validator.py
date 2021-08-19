from .base_validator import BaseValidator


class TypeValidator(BaseValidator):
    def __init__(self, key: str, type_: type) -> None:
        super().__init__(key)
        self.value_type = type_

    def valid(self, args: dict) -> bool:
        if not isinstance(args.get(self.key), self.value_type):
            # Можно добавить логику добавления в поле класса типа неверного
            # значения, чтобы потом использовать его как помощь при
            # формировании сообщения об ошибке
            return False
        return True
