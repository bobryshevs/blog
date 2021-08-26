from bson.objectid import ObjectId
from .reversible_command import ReversibleCommand
from repositories import PostRepository
from models import Post


class PostMongoCreateCommand(ReversibleCommand):
    def __init__(self, repository: PostRepository) -> None:
        self.id: ObjectId = None
        self.repository = repository
        self._post = None

    def set_post(self, post: Post):
        self._post = post

    def do(self) -> None:
        if self._post is not None:
            self.id = self.repository.create(self._post)
            return
        raise ValueError("self._post is None")

    def undo(self):
        self.repository.delete(self.id)
