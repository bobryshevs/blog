from exceptions import NotFound, BadRequest
from datetime import datetime
from bson.objectid import ObjectId
from repositories import PostRepository
from models import Post
from bson import ObjectId
from validators import (
    GetPageValidator,
    GetByIdValidator,
    DeleteValidator,
    CreateValidator
)


class PostService:

    def __init__(self, repository: PostRepository) -> None:
        self.repository = repository

    def get_page(self, args: dict) -> list[Post]:
        GetPageValidator.validate(args)
        return self.repository.get_page(
            int(args.get('page')),
            int(args.get('page_size'))
        )

    def get_by_id(self, args: dict) -> Post:
        GetByIdValidator.validate(args, self.repository)
        return self.repository.get_by_id(ObjectId(args['post_id']))

    def delete(self, args: dict) -> None:
        DeleteValidator.validate(args, self.repository)
        self.repository.delete(ObjectId(args.get('post_id')))
        return None

    def create(self, args: dict) -> Post:
        CreateValidator.validate(args)
        post = Post(
            text=args.get('text'),
            author=args.get('author'),
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
