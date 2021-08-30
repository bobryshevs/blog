from bson.objectid import ObjectId
from models.model import Model


class Post(Model):
    def __init__(self):
        self.id: ObjectId = None
        self.title: str = None
        self.content: str = None
        self.author_id: ObjectId = None
        self.comment_ids: list[ObjectId] = []

    @staticmethod
    def from_request(args: dict):
        post = Post()
        post.title = args["title"]
        post.content = args["content"]
        post.author_id = args["author_id"]
        return post

    def assign_request(self, args: dict):
        self.title = args["title"]
        self.content = args["content"]

    @property
    def str_id(self):
        return str(self.id)

    @property
    def str_comment_ids(self):
        return [str(c_id) for c_id in self.comment_ids]

    def __str__(self):
        return f"< Post [{self.id}]> \n" \
            f"{self.id = }\n" \
            f"{self.title = }\n" \
            f"{self.content = }\n" \
            f"{self.author_id = }\n" \
            f"{self.comment_ids = }"
