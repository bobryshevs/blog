class ContentValidator:
    def __init__(self, key: str) -> None:
        self.key = key

    def validate(self, args: dict) -> bool:
        """Base class for complex data checks"""
        raise NotImplementedError()
