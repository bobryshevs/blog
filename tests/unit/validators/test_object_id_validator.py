from bson.objectid import ObjectId
from validators import ObjectIdValidator


class TestContentObjectIdValidator:

    def test_valid_object_id_invalid(self):
        key = 'id'
        args = {key: 'asd123'}
        validator = ObjectIdValidator(key=key)

        assert validator.valid(args) is False

    def test_valid_object_id_valid(self):
        key = 'id'
        args = {key: ObjectId()}
        validator = ObjectIdValidator(key=key)

        assert validator.valid(args) is True
