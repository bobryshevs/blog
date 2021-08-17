from translators import comment_translator
from repositories.post_repository import PostRepository
from bson.objectid import ObjectId
from repositories import CommentRepository
from models import Comment
from exceptions import NotFound, BadRequest
from datetime import datetime


class CommentService:
    def __init__(self,
                 comment_repository: CommentRepository,
                 post_repository: PostRepository):
        self.comment_repository = comment_repository
        self.post_repository = post_repository

    def get_page(self,
                 post_id: str,
                 page: int,
                 page_size: int) -> list[Comment]:

        if not ObjectId.is_valid(post_id):
            raise BadRequest()

        if not self.post_repository.exists(ObjectId(post_id)):
            raise NotFound()

        if not isinstance(page, int) \
                or not isinstance(page_size, int) \
                or page < 1 \
                or page_size < 1:
            raise BadRequest()

        return self.comment_repository \
            .get_page(ObjectId(post_id), page, page_size)

    def get_by_id(self, comment_id: str) -> Comment:
        if not ObjectId.is_valid(comment_id):
            raise NotFound()

        comment = self.repository.get_by_id(ObjectId(comment_id))
        if comment is None:
            raise NotFound()

        return comment

    def delete(self, comment_id: str) -> None:
        if not ObjectId.is_valid(comment_id):
            raise NotFound()

        comment_id = ObjectId(comment_id)

        if not self.repository.exists(comment_id):
            raise NotFound()

        self.repository.delete(comment_id)
        return

    def create(self, post_id: str, text: str, author: str) -> Comment:
        if not ObjectId.is_valid(post_id):
            raise BadRequest()

        if not self.post_repository.exists(ObjectId(post_id)):
            raise NotFound()

        if not isinstance(text, str) or not isinstance(author, str):
            raise BadRequest()

        comment = Comment(
            text=text,
            author=author,
            post_id=ObjectId(post_id),
            date_of_creation=datetime.now()
        )

        comment.id = self.comment_repository.create(comment)
        return comment

    def update(self, post_id: str, comment_id: str, text: str):
        pass
