from datetime import datetime
from bson import ObjectId

from exceptions import (
    NotFound,
)
from repositories import PostRepository
from models import Post


class PostService:

    def __init__(self,
                 repository: PostRepository,
                 get_page_validate_service,
                 create_validate_service,
                 object_id_validate_service,
                 update_validate_service,
                 ) -> None:
        self.repository = repository
        self.get_page_validate_service = get_page_validate_service
        self.create_validate_service = create_validate_service
        self.get_by_id_validate_service = object_id_validate_service
        self.update_validate_service = update_validate_service
        self.delete_validate_service = object_id_validate_service

    def get_page(self, args: dict[str, int]) -> list[Post]:
        self.get_page_validate_service.validate(args)
        return self.repository.get_page(
            args.get('page'),
            args.get('page_size')
        )

    def get_by_id(self, args: dict) -> Post:
        self.get_by_id_validate_service.validate(args)
        post_id = ObjectId(args['id'])
        post = self.repository.get_by_id(post_id)
        if post is None:
            raise NotFound()

        return self.repository.get_by_id(post_id)

    def delete(self, args: dict[str, str]) -> None:
        self.delete_validate_service.validate(args)
        post_id = ObjectId(args.get('id'))

        if not self.repository.exists(post_id):
            raise NotFound()

        self.repository.delete(ObjectId(args.get('id')))

    def create(self, args: dict[str, str]) -> Post:
        self.create_validate_service.validate(args)
        post = Post.from_request(
            {
                "text": args.get('text'),
                "author": args.get('author'),
                "date_of_creation": datetime.now()
            }
        )
        post.id = self.repository.create(post)
        return post

    def update(self, args: dict[str, str]) -> Post:
        self.update_validate_service.validate(args)

        post_id = ObjectId(args.get('id'))

        post = self.repository.get_by_id(post_id)

        if post is None:
            raise NotFound()

        post.assign_request(args)
        self.repository.update(post)
        return post
