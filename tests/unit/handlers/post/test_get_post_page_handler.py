from mock import Mock
from werkzeug.datastructures import MultiDict

from handlers import GetPostPageHandler


class TestGetPostPageHandler:
    def test_execute(self):
        handler = GetPostPageHandler(
            token_service=Mock(),
            service=Mock(),
            presenter=Mock(),
            response_builder=Mock(),
            success_http_status_code=Mock()
        )

        request = Mock()
        request.args = MultiDict({
            "page": 1,
            "page_size": 2,
            "usless_arg": "nobody needs it"
        })
        principle = Mock()

        handler.execute(request, principle)

        handler.service.get_page.assert_called_once_with(
            {
                "page": 1,
                "page_size": 2
            }
        )
