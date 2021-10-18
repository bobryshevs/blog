
from mock import Mock

from handlers import DeletePostHandler


class TestDeletePostHandler:
    def test_execute(self):
        handler = DeletePostHandler(
            token_service=Mock(),
            service=Mock(),
            presenter=Mock(),
            response_builder=Mock(),
            success_http_status_code=Mock()
        )

        request = Mock()
        principle = Mock()

        handler.execute(request, principle)

        handler.service.delete.assert_called_once_with(
            request.view_args, principle)
