

class TypeValidator:
    def __init__(self, key: str, value_type: type) -> None:
        self.key = key
        self.value_type = value_type

    def valid(self, args: dict) -> bool:
        if not isinstance(args.get(self.key), self.value_type):
            # Можно добавить логику добавления в поле класса типа неверного
            # значения, чтобы потом использовать его как помощь при
            # формировании сообщения об ошибке
            return False
        return True
