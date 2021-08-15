from models import Post
from .translator import Translator


class PostTranslator(Translator):

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
