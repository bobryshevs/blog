
import pytest
from mock import Mock
from bson import ObjectId

from enums import HTTPStatus
from handlers import DeletePostHandler
from exceptions import (
    Unauthorized,
    Forbidden
)


class TestDeletePostHandler:
    def setup(self):
        self.token_service = Mock()
        self.service = Mock()
        self.presenter = Mock()
        self.response_builder = Mock()

        self.handler = DeletePostHandler(
            token_service=self.token_service,
            service=self.service,
            presenter=self.presenter,
            response_builder=self.response_builder
        )

    def test_execute_none_principle(self):
        with pytest.raises(Unauthorized) as err:
            self.handler.execute(request=Mock(), principle=None)

        assert err.value.code == HTTPStatus.UNAUTHORIZED
        self.service.get_by_id.assert_not_called()
        self.service.delete.assert_not_called()

    def test_execute_forbidden(self):
        request = Mock()
        request.view_args = {"id": "ObjectId"}

        post = Mock()
        post.author_id = "post_id"

        principle = Mock()
        principle.id = "principle_id"

        self.service.get_by_id.return_value = post

        with pytest.raises(Forbidden) as err:
            self.handler.execute(request=request, principle=principle)

        assert err.value.code == HTTPStatus.FORBIDDEN
        self.service.get_by_id.assert_called_once_with(request.view_args)
        self.service.delete.assert_not_called()

    def test_execute(self):
        request = Mock()
        user_id = ObjectId()
        request.view_args = {"id": str(user_id)}

        user = Mock()
        user.id = user_id

        post = Mock()
        post.author_id = user_id

        self.service.get_by_id.return_value = post

        result = self.handler.execute(request, user)

        assert isinstance(result, tuple)
        assert result == ({}, HTTPStatus.NO_CONTENT)
        self.service.get_by_id.assert_called_once_with(request.view_args)
        self.service.delete.assert_called_once_with({"id": post.id})
