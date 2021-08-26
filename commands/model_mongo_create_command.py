from bson.objectid import ObjectId
from commands import ReversibleCommand
from repositories import MongoRepository
from models import Model


class ModelMongoCreateCommand(ReversibleCommand):
    def __init__(self, repository: MongoRepository) -> None:
        self.id: ObjectId = None
        self.repository = repository

    def do(self, model: Model) -> None:
        self.id = self.repository.create(model)

    def undo(self):
        self.repository.delete(self.id)
