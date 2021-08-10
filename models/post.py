from datetime import datetime


class Post:
    def __init__(self, text: str, author: str, date_of_creation: datetime = datetime.now()):
        self.text = text
        self.author = author
        self.date_of_creation = date_of_creation


    def to_json(self):
        return str(self.__dict__)


