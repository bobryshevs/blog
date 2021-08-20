

class NonZeroStrValidator():
    def __init__(self, key: str) -> None:
        self.key = key

    def valid(self, args: dict) -> bool:
        value = args.get(self.key)
        return len(value) > 0
