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

    def test_update(self):
        self.model.id = self.repository.collection \
            .insert_one(self.document).inserted_id
        old_field_value = self.model.field
        new_field_value = "new_value"
        self.model.field = new_field_value

        inserted_field_value = self.repository.collection.find_one(
            {"_id": self.model.id})["field"]
        assert inserted_field_value == old_field_value

        self.repository.update(self.model)

        updated_field_value = self.repository.collection.find_one(
            {"_id": self.model.id})["field"]
        assert updated_field_value == new_field_value

    def test_get_one_by_field(self):
        repository = self.repository
        collection = self.repository.collection
        obj_id_list = []
        args = [
            {"first": 1, "field": "arg_1"},
            {"second": 2, "field": "arg_2"},
            {"third": 3, "field": "arg_3"},
        ]
        obj_id_list.append(collection.insert_one(args[0]).inserted_id)
        obj_id_list.append(collection.insert_one(args[1]).inserted_id)
        obj_id_list.append(collection.insert_one(args[2]).inserted_id)

        model_1 = repository.get_one_by_field("first", 1)
        model_2 = repository.get_one_by_field("second", 2)
        model_3 = repository.get_one_by_field("third", 3)

        assert model_1.id == obj_id_list[0]
        assert model_2.id == obj_id_list[1]
        assert model_3.id == obj_id_list[2]
