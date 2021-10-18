from mock import Mock

from handlers import CreatePostHandler


class TestCreatePostHandler:
    def test_execute(self):
        handler = CreatePostHandler(
            token_service=Mock(),
            service=Mock(),
            presenter=Mock(),
            response_builder=Mock(),
            success_http_status_code=Mock()
        )

        request = Mock()
        principle = Mock()

        handler.execute(request, principle)

        handler.service.create.assert_called_once_with(
            request.json, principle
        )
