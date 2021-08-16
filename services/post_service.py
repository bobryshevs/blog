from exceptions import NotFound, BadRequest
from datetime import datetime
from bson.objectid import ObjectId
from repositories import PostRepository
from models import Post
from bson import ObjectId


class PostService:

    def __init__(self, repository: PostRepository, presenter) -> None:
        self.repository = repository
        self.presenter = presenter

    def get_page(self, page: int, page_size: int) -> list[Post]:
        if not isinstance(page, int) \
                or not isinstance(page_size, int) \
                or page < 1 \
                or page_size < 1:
            raise BadRequest
        return self.repository.get_page(page, page_size)

    def get_by_id(self, post_id: str) -> Post:
        if not ObjectId.is_valid(post_id):
            raise NotFound()

        post = self.repository.get_by_id(ObjectId(post_id))
        if post is None:
            raise NotFound()

        return post

    def delete(self, post_id: str) -> None:
        if not ObjectId.is_valid(post_id):
            raise NotFound()

        post_id = ObjectId(post_id)

        if not self.repository.exists(post_id):
            raise NotFound()

        self.repository.delete(post_id)
        return

    def create(self, text: str, author: str) -> Post:
        if not isinstance(text, str) or not isinstance(author, str):
            raise BadRequest

        post = Post(
            text=text,
            author=author,
            date_of_creation=datetime.now()
        )
        post.id = self.repository.create(post)

        return post

    def update(self, post_id: str, text: str, author: str) -> Post:
        # raise exception (BadRequest + NotFound)
        self.check_valid_and_exists_id(post_id)
        post_id = ObjectId(post_id)
        post = self.repository.get_by_id(post_id)

        post.text = text
        post.author = author

        return self.repository.update(post)

    def check_valid_and_exists_id(self, post_id: str) -> bool:
        if not ObjectId.is_valid(post_id):
            raise BadRequest()

        post_id = ObjectId(post_id)

        if not self.repository.exists(post_id):
            raise NotFound()

        return True
