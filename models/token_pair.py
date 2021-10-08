

class TokenPair:
    def __init__(self, access: str, refresh: str) -> None:
        self.access: str = access
        self.refresh: str = refresh

    def json(self):
        return {
            "access": self.access,
            "refresh": self.refresh
        }

    def __eq__(self, o: "TokenPair") -> bool:
        return (self.access == o.access) and (self.refresh == o.refresh)
