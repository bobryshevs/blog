from models.post import Post
from datetime import datetime


class PostTranslator:

    def to_mongo(self, post: Post) -> dict:
        return {
            "text": post.text,
            "author": post.author,
            "create_date": post.date_of_creation
        }

    def from_dict(self, post: dict) -> Post:
        return Post(
            text=post['text'],
            author=post['author'],
            date_of_creation=datetime.now())

    def from_mongo(self, mongo_post: dict) -> Post:
        del mongo_post['_id']
        return self.from_dict(mongo_post)

