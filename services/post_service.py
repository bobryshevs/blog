from bson import ObjectId

from exceptions import (
    NotFound,
    Unauthorized,
    Forbidden
)
from repositories import PostRepository
from models import Post, User, Page
from .user_service import UserService


class PostService:

    def __init__(self,
                 repository: PostRepository,
                 user_service: UserService,
                 get_page_validate_service,
                 create_validate_service,
                 object_id_validate_service,
                 update_validate_service,
                 ) -> None:
        self.repository = repository
        self.user_service = user_service
        self.get_page_validate_service = get_page_validate_service
        self.create_validate_service = create_validate_service
        self.get_by_id_validate_service = object_id_validate_service
        self.update_validate_service = update_validate_service
        self.delete_validate_service = object_id_validate_service

    def create(self, args: dict[str, str], principle: User = None) -> Post:
        self.principle_check_none(principle)
        self.create_validate_service.validate(args)
        post = Post.from_request(
            {
                "title": args.get("title"),
                "content":  args.get("content"),
                "author_id": principle.id,
            }
        )
        post.id = self.repository.create(post)
        return post

    def get_by_id(self, args: dict) -> Post:
        self.get_by_id_validate_service.validate(args)
        post_id = ObjectId(args["id"])
        post = self.repository.get_by_id(post_id)
        if post is None:
            raise NotFound({"msg": "post with given id not found"})
        return post

    def update(self, args: dict[str, str], principle: User = None) -> Post:
        self.principle_check_none(principle)
        self.update_validate_service.validate(args)

        post: Post = self.get_by_id(args["id"])

        if post.author_id != principle.id:
            msg = "You can't update a post that you aren't the author of"
            raise Forbidden({"msg": msg})

        post.assign_request(args)
        self.repository.update(post)

        return post

    def delete(self, args: dict[str, str], principle: User = None) -> None:
        self.principle_check_none(principle)
        self.delete_validate_service.validate(args)

        post: Post = self.get_by_id(args["id"])

        if principle.id != post.author_id:
            msg = "You can't delete a post that you aren't the author of"
            raise Forbidden({"msg": msg})

        self.repository.delete(post.id)

    def get_page(self, args: dict[str, str]) -> Page:
        self.get_page_validate_service.validate(args)
        return self.repository.get_page(
            int(args.get("page")),
            int(args.get("page_size"))
        )

    def principle_check_none(self, principle):
        if principle is None:
            raise Unauthorized(
                {
                    "msg": "only an authorized user can perform this action"
                }
            )
