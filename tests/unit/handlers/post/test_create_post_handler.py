from mock import Mock

from handlers.base_handler import BaseHandler


class TestCreatePostHandler:
    def test_execute(self):
        token_service = Mock()
        service = Mock()
        presenter = Mock()
        response_builder = Mock()

        service_create_value = object()
        service.create_return_value = service_create_value
        request = Mock()
        request.json = {}
        principle = object()
        principle.id = "id"

        handler = BaseHandler(
            token_service=token_service,
            service=service,
            presenter=presenter,
            response_builder=response_builder
        )

        result = handler.execute(request, principle)

        service.create.assert_called_once_with({} | {"author_id": "id"})
        presenter.to_json.assert_called_once_with(service_create_value)
        # TODO: presenter assert call
