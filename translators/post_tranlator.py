from models.post import Post
from datetime import datetime


class PostTranslator:

    def to_mongo(self, post: Post) -> dict:
        return {
            "text": post.text,
            "author": post.author,
            "date_of_creation": post.date_of_creation
        }

    def from_dict(self, post: dict) -> Post:
        return Post(
            text=post['text'],
            author=post['author'],
            date_of_creation=datetime.now().isoformat())

    def from_mongo(self, mongo_post: dict) -> Post:
        post = Post(
            text=mongo_post['text'], 
            author=mongo_post['author'],
            date_of_creation=mongo_post['date_of_creation'])
        post.m_id = str(mongo_post['_id'])
        return post
    


