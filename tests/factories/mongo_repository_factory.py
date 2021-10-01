from bson import ObjectId

from structure import mongo_client
from repositories import MongoRepository


class MongoRepositoryFactory:
    def get(self):
        return MongoRepository(
            translator=MongoTestModelTranslator(),
            collection=mongo_client.blog_database.test_collection
        )


class MongoTestModel:
    def __init__(self) -> None:
        self.id: ObjectId = None
        self.field: str = None


class MongoTestModelTranslator:
    def to_document(self, model: MongoTestModel) -> dict:
        return {"field": model.field}

    def from_document(self, document: dict) -> MongoTestModel:
        model = MongoTestModel()
        model.id = document["_id"]
        model.field = document["field"]
        return model
