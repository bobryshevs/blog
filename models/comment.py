from datetime import datetime
from bson.objectid import ObjectId
from .model import Model


class Comment(Model):
    def __init__(self,
                 text: str,
                 author: str,
                 post_id: ObjectId, 
                 date_of_creation: datetime,
                 m_id: ObjectId = None
                 ):
        self.id = m_id
        self.text: str = text
        self.author: str = author
        self.post_id: ObjectId = post_id
        self.date_of_creation: str = date_of_creation
