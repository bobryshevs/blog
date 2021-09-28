from bson import ObjectId
from .mongo_repository import MongoRepository
from models import User

class UserRepository(MongoRepository):
    def create(self, model: User) -> ObjectId:
        return super().create(model)
