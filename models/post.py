from datetime import datetime

from datetime import datetime

from bson.objectid import ObjectId


class Post:
    def __init__(self,
                 text: str,
                 author: str,
                 date_of_creation: datetime = None,
                 m_id=None):
        self.id = m_id
        self.text: str = text
        self.author: str = author
        self.date_of_creation: datetime = date_of_creation
        # Todo: проверка корректности даты
