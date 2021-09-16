

class PresenceValidator():
    def __init__(self, key: str) -> None:
        self.key = key

    def valid(self, args: dict) -> bool:
        return self.key in args

    def error(self) -> str:
        return f"Error in [{self.key}]. Missed required parameter."