from mock import Mock

from handlers import GetPostHandler


class TestGetPostHandler:
    def test_execute(self):
        handler = GetPostHandler(
            token_service=Mock(),
            service=Mock(),
            presenter=Mock(),
            response_builder=Mock(),
            success_http_status_code=Mock()
        )

        request = Mock()
        principle = Mock()

        handler.execute(request, principle)

        handler.service.get_by_id.assert_called_once_with(request.view_args)
