from datetime import datetime
from bson.objectid import ObjectId


from models.model import Model


class Post(Model):
    def __init__(self,
                 text: str = None,
                 author: str = None,
                 date_of_creation: datetime = None,
                 m_id: ObjectId = None):
        self.id = m_id
        self.text: str = text
        self.author: str = author
        self.date_of_creation: datetime = date_of_creation

    @staticmethod
    def from_request(args: dict):
        post = Post()
        post.text = args['text']
        post.author = args['author']
        post.date_of_creation = args['date_of_creation']

        return post

    def assign_request(self, args: dict):
        self.text = args['text']
        self.author = args['author']
