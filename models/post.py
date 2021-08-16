from datetime import datetime
from bson.objectid import ObjectId
from .model import Model


class Post:
    def __init__(self,
                 text: str,
                 author: str,
                 date_of_creation: datetime = None,
                 m_id: ObjectId = None):
        self.id = m_id
        self.text: str = text
        self.author: str = author
        self.date_of_creation: datetime = date_of_creation
        # Todo: проверка корректности даты
