from bson import ObjectId
from .mongo_repository import MongoRepository
from models import User


class UserRepository(MongoRepository):

    def create(self, model: User) -> ObjectId:
        if self.exists_email(model.email):
            return None
        return super().create(model)

    def exists_email(self, email: str) -> bool:
        return self.collection.find_one({"email": email}) is not None

    def get_user_token(self, page: int, page_size: int) -> list[User]:
        pipeline = [
            {"$skip": (page - 1) * page_size},
            {"$project": {"tokens": 1}},
            {"$limit": page_size}
        ]
        docs = self.collection.aggregate(pipeline)
        users = [self.translator.from_document(doc) for doc in docs]
        return users

    def update_user_token(self, user: User) -> None:
        doc = self.translator.to_document(user)
        self.collection.update_one(
            {"_id": user.id},
            {"$set": {"tokens": doc["tokens"]}}
        )
