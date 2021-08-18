from re import A
from exceptions import NotFound, BadRequest
from datetime import datetime
from bson.objectid import ObjectId
from repositories import PostRepository
from models import Post
from bson import ObjectId


class PostService:

    def __init__(self,
                 repository: PostRepository,
                 get_page_validate_service,
                 create_validate_service,
                 get_by_id_validate_service) -> None:
        self.repository = repository
        self.get_page_validate_service = get_page_validate_service
        self.create_validate_service = create_validate_service
        self.get_by_id_validate_service = get_by_id_validate_service

    def get_page(self, args: dict) -> list[Post]:
        self.get_page_validate_service.validate(args)
        return self.repository.get_page(
            int(args.get('page')),
            int(args.get('page_size'))
        )

    def get_by_id(self, args: dict) -> Post:
        """
            args: {
                "post_id": str -> ObjectId
            }
        """
        self.get_by_id_validate_service.validate(args)
        post_id = ObjectId(args['post_id'])

        if not self.repository.exists(post_id):
            raise NotFound
        
        return self.repository.get_by_id(post_id)

    def delete(self, args: dict) -> None:
        # DeleteValidator.validate(args, self.repository)
        self.repository.delete(ObjectId(args.get('post_id')))
        return None

    def create(self, args: dict) -> Post:
        """
            args: {
                "text": str,
                "author": str, len > 0
            }
        """
        self.create_validate_service.validate(args)
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
