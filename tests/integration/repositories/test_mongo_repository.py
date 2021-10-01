from bson import ObjectId

from tests.factories import (
    MongoTestModel,
    mongo_repository_factory,
    mongo_test_model_translator
)


class TestMongoRepository:
    def setup(self):
        self.model = MongoTestModel()
        self.model.field = "field"
        self.document = mongo_test_model_translator.to_document(self.model)
        self.repository = mongo_repository_factory.get()

    def teardown(self):
        self.repository.collection.delete_many({})

    def test_create(self):
        self.model.id = self.repository.create(self.model)
        document = self.repository.collection.find_one({"_id": self.model.id})

        assert document["field"] == self.model.field
        assert document["_id"] == self.model.id

    def test_get_by_id_model(self):
        self.model.id = self.repository.collection \
            .insert_one(self.document).inserted_id
        result = self.repository.get_by_id(self.model.id)

        assert isinstance(result, MongoTestModel)
        assert self.model.field == result.field
        assert self.model.id == result.id

    def test_get_by_id_none(self):
        random_id = ObjectId()
        result = self.repository.get_by_id(random_id)
        assert result is None

    def test_delete(self):
        self.model.id = self.repository.collection \
            .insert_one(self.document).inserted_id

        assert self.repository.collection.find_one(
            {"_id": self.model.id}) is not None

        self.repository.delete(self.model.id)

        assert self.repository.collection.find_one(
            {"_id": self.model.id}) is None
