from bson.objectid import ObjectId
from models.model import Model


class Post(Model):
    def __init__(self):
        self.id: ObjectId = None
        self.title: str = None
        self.content: str = None
        self.author_id: ObjectId = None
        self.comment_ids: list[ObjectId] = None

    @staticmethod
    def from_request(args: dict):
        post = Post()
        post.title = args['title']
        post.content = args['content']
        post.author_id = args['author_id']
        return post

    def assign_request(self, args: dict):
        self.title = args['title']
        self.content = args['content']
