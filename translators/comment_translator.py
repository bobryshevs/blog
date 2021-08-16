from .translator import Translator
from models import Comment


class CommentTranslator(Translator):

    def to_document(self, comment: Comment) -> dict:
        return {
            "text": comment.text,
            "author": comment.author,
            "post_id": comment.post_id,
            "date_of_creation": comment.date_of_creation
        }

    def from_document(self, mongo_comment: dict) -> Comment:
        return Comment(
            m_id=mongo_comment['_id'],
            text=mongo_comment['text'],
            author=mongo_comment['author'],
            post_id=mongo_comment['post_id'],
            date_of_creation=mongo_comment['date_of_creation']
        )
