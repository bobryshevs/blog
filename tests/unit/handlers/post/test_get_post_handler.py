from mock import Mock

from handlers import GetPostHandler
from enums import HTTPStatus


class TestGetPostHandler:

    def test_execute(self):
        token_service = Mock()
        service = Mock()
        presenter = Mock()
        response_builder = Mock()

        post = object()
        service.get_by_id.return_value = post

        dict_post = {"id": "ObjectId"}
        presenter.to_json.return_value = dict_post

        request = Mock()
        view_args = {"id": "12345678"}
        request.view_args = view_args

        handler = GetPostHandler(
            token_service=token_service,
            service=service,
            presenter=presenter,
            response_builder=response_builder
        )

        result = handler.execute(request, object)

        assert isinstance(result, tuple)
        service.get_by_id.assert_called_once_with(view_args)
        presenter.to_json.assert_called_once_with(post)
        assert result == (dict_post, HTTPStatus.OK)
