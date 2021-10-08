from bson import ObjectId


class ObjectIdValidator():
    def __init__(self, key: str) -> None:
        self.key = key

    def valid(self, args: dict) -> bool:
        return ObjectId.is_valid(args.get(self.key))

    def error(self) -> str:
        return f"Error in [{self.key}]. Incorrect ObjectId was given."
