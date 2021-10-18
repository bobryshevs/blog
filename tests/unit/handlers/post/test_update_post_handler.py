from mock import Mock

from handlers import UpdatePostHandler


class TestUpdatePostHandler:
    def test_execute(self):
        handler = UpdatePostHandler(
            token_service=Mock(),
            service=Mock(),
            presenter=Mock(),
            response_builder=Mock(),
            success_http_status_code=Mock()
        )

        request = Mock()
        request.json = {"json": "args"}
        request.view_args = {"view": "args"}
        principle = Mock()

        handler.execute(request, principle)

        handler.service.update.assert_called_once_with(
            {"json": "args", "view": "args"},
            principle
        )
