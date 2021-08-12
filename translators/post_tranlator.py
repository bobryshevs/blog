from models.post import Post
from datetime import datetime


class PostTranslator:

    def to_document(self, post: Post) -> dict:
        return {
            "text": post.text,
            "author": post.author,
            "date_of_creation": post.date_of_creation
        }

    def from_document(self, mongo_post: dict) -> Post:
        post = Post(
            text=mongo_post['text'],
            author=mongo_post['author'],
            date_of_creation=mongo_post['date_of_creation'],
            m_id=mongo_post['_id'])
        return post
