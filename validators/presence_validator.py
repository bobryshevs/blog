

class PresenceValidator():
    def __init__(self, key: str) -> None:
        self.key = key

    def valid(self, args: dict) -> bool:
        if self.key not in args:
            return False

        return True
