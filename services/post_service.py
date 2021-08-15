from datetime import datetime
from validators.post_validator import PostValidator
from bson.objectid import ObjectId
from repositories import PostRepository
from models import Post
from bson import ObjectId


class PostService:

    def __init__(self, repository: PostRepository, presenter) -> None:
        self.repo = repository
        self.presenter = presenter

    def get_by_id(self, post_id: ObjectId) -> Post:
        self.repo.exists(post_id)
        return self.repo.get_by_id(post_id)

    def get_page(self, page: int, page_size: int) -> list[Post]:
        return self.repo.get_page(page, page_size)

    def get_multiple_by_IDs(self, IDs: list[ObjectId]) -> list[Post]:
        return [
            self.repo.get_by_id(post_id)
            for post_id in IDs
        ]

    def delete(self, post_id: ObjectId) -> ObjectId:
        if not self.repo.exists(post_id):
            return None
        
        self.repo.delete(post_id)
        return post_id

    def create(self, text: str, author: str) -> ObjectId:
        post = Post(
            text=text,
            author=author,
            date_of_creation=datetime.now()
        )
        post_id = self.repo.create(post)
        return post_id
    
    def update(self, post_id: ObjectId, text: str, author: str) -> Post:
        post = Post(
            text=text,
            author=author,
            m_id=post_id
        )
        return self.repo.update(post)

