from mock import Mock
from enums import HTTPStatus

from handlers import CreatePostHandler


class TestCreatePostHandler:
    def test_execute(self):
        token_service = Mock()
        service = Mock()
        presenter = Mock()
        response_builder = Mock()

        service_create_value = Mock()
        service.create.return_value = service_create_value
        request = Mock()
        request.json = {}
        principle = Mock()
        principle.id = "id"
        presenter.to_json.return_value = {}
        expected_service_create_args = {} | {"author_id": "id"}

        handler = CreatePostHandler(
            token_service=token_service,
            service=service,
            presenter=presenter,
            response_builder=response_builder
        )

        result = handler.execute(request, principle)

        service.create.assert_called_once_with(expected_service_create_args)
        presenter.to_json.assert_called_once_with(service_create_value)
        assert result == ({}, HTTPStatus.CREATED)
