from exceptions import NotFound, BadRequest
from datetime import datetime
from bson.objectid import ObjectId
from repositories import PostRepository
from models import Post
from bson import ObjectId


class PostService:

    def __init__(self, repository: PostRepository, presenter) -> None:
        self.repo = repository
        self.presenter = presenter

    def get_page(self, page: int, page_size: int) -> list[Post]:
        if not isinstance(page, int) \
                or not isinstance(page_size, int) \
                or page < 1 \
                or page_size < 1:
            raise BadRequest
        return self.repo.get_page(page, page_size)

    def get_by_id(self, post_id: str) -> Post:
        # raise exception if something is wrong with data
        self.check_valid_and_exists_id(post_id)
        post_id = ObjectId(post_id)
        return self.repo.get_by_id(post_id)

    def delete(self, post_id: str) -> ObjectId:
        # raise exception if something is wrong with data
        self.check_valid_and_exists_id(post_id)
        post_id = ObjectId(post_id)
        self.repo.delete(post_id)
        return post_id

    def create(self, text: str, author: str) -> ObjectId:
        if not isinstance(text, str) or not isinstance(author, str):
            raise BadRequest

        post = Post(
            text=text,
            author=author,
            date_of_creation=datetime.now()
        )

        post_id = self.repo.create(post)
        return post_id

    def update(self, post_id: str, text: str, author: str) -> Post:
        # raise exception if something is wrong with data
        self.check_valid_and_exists_id(post_id)
        post_id = ObjectId(post_id)
        post = self.repo.get_by_id(post_id)

        post.text = text
        post.author = author

        return self.repo.update(post)

    def check_valid_and_exists_id(self, post_id: str) -> bool:
        if not ObjectId.is_valid(post_id):
            raise BadRequest

        post_id = ObjectId(post_id)

        if not self.repo.exists(post_id):
            raise NotFound

        return True
