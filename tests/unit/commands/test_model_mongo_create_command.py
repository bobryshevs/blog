import pytest
from bson import ObjectId
from mock import Mock

from commands import ModelMongoCreateCommand
from models import Post


class TestModelMongoCreateCommand:

    def test_do(self):
        repository = Mock()
        model_id = ObjectId()
        repository.create.return_value = model_id
        post = Post()

        command = ModelMongoCreateCommand(repository=repository)
        command.do(post)

        assert model_id == command.id
        repository.create.assert_called_once_with(post)

    def test_undo(self):
        repository = Mock()
        model_id = ObjectId()

        command = ModelMongoCreateCommand(repository=repository)
        command.id = model_id
        command.undo()

        repository.delete.assert_called_once_with(model_id)
