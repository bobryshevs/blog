from bson import ObjectId
from .token_pair import TokenPair


class UserToken:
    def __init__(self) -> None:
        self.id: ObjectId = None
        self.tokens: list[TokenPair] = []
