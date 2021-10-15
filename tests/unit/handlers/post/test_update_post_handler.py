import pytest
from mock import Mock
from bson import ObjectId

from handlers import UpdatePostHandler
from enums import HTTPStatus
from exceptions import Unauthorized, Forbidden


class TestUpdatePostHandler:
    def setup(self):
        self.token_service = Mock()
        self.service = Mock()
        self.presenter = Mock()
        self.response_builder = Mock()

        self.handler = UpdatePostHandler(
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
        request.json = {"post": "fields"}

        user = Mock()
        user.id = user_id

        post = Mock()
        post.author_id = user_id

        new_post = Mock()
        json_post = {"json": "post"}

        self.service.get_by_id.return_value = post
        self.service.update.return_value = new_post
        self.presenter.to_json.return_value = json_post
        update_args =  \
            request.json | {"author_id": post.author_id} | request.view_args
        print(update_args, flush=True)
        result = self.handler.execute(request, user)

        assert isinstance(result, tuple)
        assert result == (json_post, HTTPStatus.OK)
        self.service.get_by_id.assert_called_once_with(request.view_args)
        self.service.update.assert_called_once_with(update_args)
