from datetime import datetime


class Post:
    def __init__(self, text: str, author: str):
        self.text: str = text
        self.author: str = author
        self.date_of_creation: str = datetime.now().isoformat()

    def to_json(self) -> dict:
        return self.__dict__



